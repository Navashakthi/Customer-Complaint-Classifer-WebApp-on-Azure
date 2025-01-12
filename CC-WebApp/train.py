from azure.storage.blob import BlobServiceClient
import pandas as pd
from io import StringIO
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import joblib


# Replace with your Azure Storage Account name and key
account_name = "your-azure-account"
account_key = "account-key"

# Initialize the BlobServiceClient with the account name and key
blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)

# Specify the container name and blob name (the file you want to access)
container_name = "azure-container-name"
blob_name = "data.csv"

# Get the blob client to interact with the file
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

# Download the blob content as a string (CSV file)
blob_data = blob_client.download_blob()
csv_content = blob_data.content_as_text()

# Convert the CSV content to a pandas DataFrame
df_csv = pd.read_csv(StringIO(csv_content))
df = df_csv[pd.notnull(df_csv['Consumer complaint narrative'])]
col = ['Product', 'Consumer complaint narrative']
df = df[col]
df.columns = ['Product', 'Consumer_complaint_narrative']
df['category_id'] = df['Product'].factorize()[0]
from io import StringIO
category_id_df = df[['Product', 'category_id']].drop_duplicates().sort_values('category_id')
category_to_id = dict(category_id_df.values)
id_to_category = dict(category_id_df[['category_id', 'Product']].values)
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english', max_features=10000)

features = tfidf.fit_transform(df.Consumer_complaint_narrative).toarray()
labels = df.category_id
print(features.shape)

# Step 1: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(df['Consumer_complaint_narrative'], df['Product'], random_state=0)

# Step 2: Preprocessing
count_vect = CountVectorizer()
tfidf_transformer = TfidfTransformer()

X_train_counts = count_vect.fit_transform(X_train)
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

X_test_counts = count_vect.transform(X_test)
X_test_tfidf = tfidf_transformer.transform(X_test_counts)

# Step 3: Train the Model
clf = MultinomialNB().fit(X_train_tfidf, y_train)

# Step 4: Make Predictions
y_pred = clf.predict(X_test_tfidf)

# Step 5: Evaluate the Model
accuracy = accuracy_score(y_test, y_pred)
class_report = classification_report(y_test, y_pred, zero_division=0)

print(f"Accuracy: {accuracy}")
print("\nClassification Report:")
print(class_report)

# Step 6: Save the Model and Preprocessing
joblib.dump(clf, 'naive_bayes_model.pkl')
joblib.dump(count_vect, 'count_vectorizer.pkl')
joblib.dump(tfidf_transformer, 'tfidf_transformer.pkl')
