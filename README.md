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

## Getting Started

### Prerequisites

1. **Azure Machine Learning**: For training the model.
2. **Azure Blob Storage**: To store and fetch training data.
3. **Docker**: To build and run the Docker container.
4. **Azure Container Registry**: For storing the Docker image.
5. **Python 3.8+**

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


## Example Use Case

1. A user provides a customer complaint as input via the web interface.
2. The trained Naive Bayes model predicts the category of the complaint.
3. The result is displayed instantly on the Gradio UI.
![image](https://github.com/user-attachments/assets/eee45471-5ee2-4bb5-b9f8-9b7987a8c37e)


## Deployment Architecture

1. **Model Training**:
   - Executed in an Azure Machine Learning notebook.
2. **Containerization**:
   - The trained model and serving pipeline (`app.py`) are packaged into a Docker image.
3. **Deployment**:
   - The Docker image is stored in Azure Container Registry.
   - The application is deployed on an Azure WebApp.

## Deploying Gradio App on Azure Web App Services

This below guide explains the step-by-step process to deploy a Gradio-based application for classifying customer complaints on **Azure Web App Services** using a container image stored in **Azure Container Registry (ACR)**.

## Prerequisites

1. **Azure Account**: Ensure you have an active Azure subscription.
2. **Azure CLI**: Installed and configured. [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
3. **Docker**: Installed and configured. [Install Docker](https://docs.docker.com/get-docker/)
4. **Azure Container Registry (ACR)**: Set up to store Docker images. [Learn more about ACR](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-intro)
5. A **Docker image** of the Gradio app, pushed to ACR.


### Step 1: Prepare the Docker Image
Image built and pushed to ACR in previous stage.

Here are the steps to create an Azure Web App using the Azure Portal (console):  

### **Step 2: Create a Resource Group (Optional)**  
1. In the search bar, type **Resource Groups** and click on it.  
2. Click **+ Create**.  
3. Provide the following details:  
   - **Subscription:** Choose your Azure subscription.  
   - **Resource Group Name:** Enter a unique name for the group (e.g., `my-webapp-rg`).  
   - **Region:** Select the region closest to your users.  
4. Click **Review + Create**, then **Create**.

### **Step 3: Create the Azure Web App**  
1. In the search bar, type **App Services** and click on it.  
2. Click **+ Create**.  
3. Fill in the following details on the **Basics** tab:  
   - **Subscription:** Choose your Azure subscription.  
   - **Resource Group:** Select the resource group you created earlier.  
   - **Name:** Enter a unique name for your web app (e.g., `my-webapp`).  
   - **Publish:** Choose **Code** or **Docker Container** depending on your deployment.  
   - **Runtime stack:** If you selected **Code**, choose your language stack (e.g., Python, Node.js, Java).  
   - **Operating System:** Choose **Windows** or **Linux** based on your requirements.  
   - **Region:** Select the region where the app will be hosted.  

### **Step 4: Configure App Service Plan**  
1. Under **App Service Plan**, either select an existing plan or create a new one:  
   - Click **Create New**.  
   - Provide a name for the plan.  
   - Choose the **Pricing Tier** (e.g., Free, Shared, or Premium).  
   - Click **Apply**.  

### **Step 5: Review and Create**  
1. Click **Next** through the tabs (e.g., Monitoring, Tags). These are optional configurations:  
   - **Monitoring:** Enable **Application Insights** if you want monitoring and telemetry.  
2. Review your selections.  
3. Click **Create**.  

### **Step 6: Deploy Your Application**  
After the deployment completes:  
1. Go to the **Overview** page of your Web App.  
2. Note the **URL** of your app.  
3. Deploy your application by:  
   - Using **FTP**, **Local Git**, or **GitHub Actions**.  
   - Uploading a Docker image if you selected a containerized app.  

### **Step 7: Verify and Test**  
1. Open the **URL** in a browser to verify your web app is running.  
2. Test any API or application features you've deployed.  

### **Step 7: Configure PORT**  
Add website port number to environment variable as settings > Environment variables > Add new > WEBSITES_PORT = 8080

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


## Additional Resources

- [Azure Web App Documentation](https://learn.microsoft.com/en-us/azure/app-service/)
- [Azure CLI Reference](https://learn.microsoft.com/en-us/cli/azure/reference-index)
- [Gradio Documentation](https://gradio.app/docs/)


By following these steps, you can successfully deploy the Gradio app for classifying customer complaints on Azure Web App Services.



## License

This project is licensed under the MIT License. See the `LICENSE` file for details.


