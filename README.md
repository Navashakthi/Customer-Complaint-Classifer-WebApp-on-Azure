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

## Example Use Case

1. A user provides a customer complaint as input via the web interface.
2. The trained Naive Bayes model predicts the category of the complaint.
3. The result is displayed instantly on the Gradio UI.
![image](https://github.com/user-attachments/assets/eee45471-5ee2-4bb5-b9f8-9b7987a8c37e)

---

## Deployment Architecture

1. **Model Training**:
   - Executed in an Azure Machine Learning notebook.
2. **Containerization**:
   - The trained model and serving pipeline (`app.py`) are packaged into a Docker image.
3. **Deployment**:
   - The Docker image is stored in Azure Container Registry.
   - The application is deployed on an Azure WebApp.

---
# Deploying Gradio App on Azure Web App Services

This below guide explains the step-by-step process to deploy a Gradio-based application for classifying customer complaints on **Azure Web App Services** using a container image stored in **Azure Container Registry (ACR)**.

## Prerequisites

1. **Azure Account**: Ensure you have an active Azure subscription.
2. **Azure CLI**: Installed and configured. [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
3. **Docker**: Installed and configured. [Install Docker](https://docs.docker.com/get-docker/)
4. **Azure Container Registry (ACR)**: Set up to store Docker images. [Learn more about ACR](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-intro)
5. A **Docker image** of the Gradio app, pushed to ACR.

---

## Step 1: Prepare the Docker Image
Image built and pushed to ACR in previous stage.

## Step 2: Create a New Web App

1. **Log in to Azure**:
   ```bash
   az login
   ```

2. **Create a resource group** (if not already created):
   ```bash
   az group create --name <resource-group-name> --location <location>
   ```

3. **Create a new Azure Web App for Containers**:
   ```bash
   az webapp create \
     --resource-group <resource-group-name> \
     --plan <app-service-plan-name> \
     --name <webapp-name> \
     --deployment-container-image-name <acr-login-server>/customer-complaint-classifier:latest
   ```

   - Replace `<resource-group-name>`, `<app-service-plan-name>`, and `<webapp-name>` with appropriate values.
   - Ensure `<acr-login-server>` matches your Azure Container Registry login server (e.g., `myregistry.azurecr.io`).

---

## Step 3: Configure Deployment Settings

1. **Set ACR authentication for the Web App**:
   ```bash
   az webapp config container set \
     --name <webapp-name> \
     --resource-group <resource-group-name> \
     --docker-custom-image-name <acr-login-server>/customer-complaint-classifier:latest \
     --docker-registry-server-url https://<acr-login-server> \
     --docker-registry-server-user <acr-username> \
     --docker-registry-server-password <acr-password>
   ```

   - Replace `<acr-username>` and `<acr-password>` with your ACR credentials.
   - You can retrieve ACR credentials using:
     ```bash
     az acr credential show --name <acr-name>
     ```
---

## Step 4: Verify Deployment

1. **Check the deployment status**:
   ```bash
   az webapp show --name <webapp-name> --resource-group <resource-group-name> --query state
   ```
   The state should return `Running`.

2. **Access the application**:
   - Open your browser and navigate to: `https://<webapp-name>.azurewebsites.net`
   - The Gradio app should now be accessible.

---

## Troubleshooting

- **Logs**:
  Retrieve logs to debug issues:
  ```bash
  az webapp log tail --name <webapp-name> --resource-group <resource-group-name>
  ```

- **Restart the web app**:
  ```bash
  az webapp restart --name <webapp-name> --resource-group <resource-group-name>
  ```

---

## Additional Resources

- [Azure Web App Documentation](https://learn.microsoft.com/en-us/azure/app-service/)
- [Azure CLI Reference](https://learn.microsoft.com/en-us/cli/azure/reference-index)
- [Gradio Documentation](https://gradio.app/docs/)

---

By following these steps, you can successfully deploy the Gradio app for classifying customer complaints on Azure Web App Services.



## License

This project is licensed under the MIT License. See the `LICENSE` file for details.


