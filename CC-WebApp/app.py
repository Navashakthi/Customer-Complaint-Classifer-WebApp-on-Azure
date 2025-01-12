import gradio as gr
import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

# Load the saved model and preprocessing objects
clf = joblib.load('naive_bayes_model.pkl')
count_vect = joblib.load('count_vectorizer.pkl')
tfidf_transformer = joblib.load('tfidf_transformer.pkl')

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

# Launch the Gradio app
iface.launch(share=True)
