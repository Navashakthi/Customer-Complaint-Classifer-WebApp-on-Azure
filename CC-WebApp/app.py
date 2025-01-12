import gradio as gr
import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import os
import uvicorn

# Load the saved model and preprocessing objects
model_path = os.path.join(os.getcwd(), 'naive_bayes_model.pkl')
countvec = os.path.join(os.getcwd(), 'count_vectorizer.pkl')
tfidf_path = os.path.join(os.getcwd(), 'tfidf_transformer.pkl')
clf = joblib.load(model_path)
count_vect = joblib.load(countvec)
tfidf_transformer = joblib.load(tfidf_path)
print("--------Model Files loaded successfully---------")

# Define a function that will be used for prediction
def predict_complaint_category(complaint_text):
    # Preprocess the input text like the training data
    complaint_counts = count_vect.transform([complaint_text])
    complaint_tfidf = tfidf_transformer.transform(complaint_counts)
    
    # Predict the category
    predicted_category = clf.predict(complaint_tfidf)
    
    return predicted_category[0]

# Create the Gradio interface
iface = gr.Interface(
    fn=predict_complaint_category,  # The function to call
    inputs=gr.Textbox(lines=2, placeholder="Enter complaint text here..."),  # Input box for the complaint text
    outputs=gr.Label(),  # Output label for predicted category
    title="Complaint Category Classifier",  # Title of the web interface
    description="Enter a complaint text, and this model will predict the category of the product.",  # Description
)

print("-----Interface Created Successfully--------")

# Launch the Gradio app on port 8080
iface.launch(server_name="0.0.0.0", server_port=8080, share=True)
