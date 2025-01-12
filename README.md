# Customer-Complaint-Classifer-WebApp-on-Azure

This repository contains a **Customer Complaint Classifier** implemented as a web application using Gradio. The model is trained using a Naive Bayes classifier to classify customer complaints. The application is hosted on port 8080 and can be deployed as a Docker container.

## Repository Structure

```
CC-WebApp/
├── train.py           # Script to train and save the Naive Bayes model
├── app.py             # Gradio-based application to use the trained model
├── requirements.txt   # Python dependencies
├── Dockerfile         # Docker configuration for the application
```

## Features

- **Model Training**: The `train.py` script fetches data from Azure Blob Storage, trains a Naive Bayes model, and saves the trained model to a directory.
- **Web Application**: The `app.py` script provides a Gradio-based user interface for end users to classify customer complaints using the trained model.
- **Dockerized Deployment**: The application can be containerized using the `Dockerfile` and pushed to Azure Container Registry for scalable deployment.

---

## Getting Started

### Prerequisites

1. **Azure Machine Learning**: For training the model.
2. **Azure Blob Storage**: To store and fetch training data.
3. **Docker**: To build and run the Docker container.
4. **Azure Container Registry**: For storing the Docker image.
5. **Python 3.9+**

---

## Step-by-Step Guide

### 1. Model Training

1. Open the Azure Machine Learning notebook console.
2. Clone this repository:
   ```bash
   git clone <repository-url>
   cd CC-WebApp
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the `train.py` script to train the model:
   ```bash
   python train.py
   ```
   - **Input**: The script fetches training data from Azure Blob Storage.
   - **Output**: A trained Naive Bayes model saved in a local directory (e.g., `./models`).

---

### 2. Building and Deploying the Application

1. Build the Docker image:
   ```bash
   docker build -t customer-complaint-classifier:latest .
   ```
2. Tag the Docker image:
   ```bash
   docker tag customer-complaint-classifier:latest <azure-container-registry-url>/customer-complaint-classifier:latest
   ```
3. Log in to Azure Container Registry:
   ```bash
   az acr login --name <registry-name>
   ```
4. Push the image to the Azure Container Registry:
   ```bash
   docker push <azure-container-registry-url>/customer-complaint-classifier:latest
   ```

---

### 3. Running the Application Locally

1. Pull the Docker image (if not built locally):
   ```bash
   docker pull <azure-container-registry-url>/customer-complaint-classifier:latest
   ```
2. Run the Docker container:
   ```bash
   docker run -p 8080:8080 customer-complaint-classifier:latest
   ```
3. Access the Gradio application at `http://localhost:8080`.

---

## Files Description

### 1. `train.py`
This script:
- Fetches training data from Azure Blob Storage.
- Trains a Naive Bayes model on the data.
- Saves the trained model to a specified directory.

### 2. `app.py`
This script:
- Loads the trained model.
- Provides a Gradio user interface to classify customer complaints.

### 3. `requirements.txt`
Lists all the dependencies required for training and serving the model. Key dependencies include:
- `sklearn`
- `gradio`
- `azure-storage-blob`

### 4. `Dockerfile`
Defines the containerization process for the Gradio application:
- Sets up the Python environment.
- Installs the required dependencies.
- Copies the application files and exposes port 8080.
- Defines the command to run `app.py`.

---

## Example Use Case

1. A user provides a customer complaint as input via the web interface.
2. The trained Naive Bayes model predicts the category of the complaint.
3. The result is displayed instantly on the Gradio UI.

---

## Deployment Architecture

1. **Model Training**:
   - Executed in an Azure Machine Learning notebook.
2. **Containerization**:
   - The trained model and serving pipeline (`app.py`) are packaged into a Docker image.
3. **Deployment**:
   - The Docker image is stored in Azure Container Registry.
   - The application is deployed on an Azure Kubernetes Service (AKS) or similar.

---


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.


