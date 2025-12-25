
Python Code:
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from azure.storage.blob import BlobServiceClient
import requests

app = Flask(__name__, static_folder="static")
CORS(app)  # Enable CORS for cross-origin requests

# Azure Blob Storage Configuration
AZURE_STORAGE_CONNECTION_STRING = "YOUR_CONNECTION_STRING_HERE"  # Replace with your Azure Storage connection string
CONTAINER_NAME = "images"  # Replace with your container name
blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

# Custom Vision Configuration
PREDICTION_ENDPOINT = "YOUR_PREDICTION_ENDPOINT_HERE"
PREDICTION_KEY = "YOUR_PREDICTION_KEY_HERE"

def upload_to_blob_storage(file, blob_name):
    
    try:
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(file, overwrite=True)
        print(f"File '{blob_name}' uploaded to Blob Storage.")
    except Exception as e:
        print(f"An error occurred during Blob upload: {e}")

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/analyze', methods=['POST'])
def analyze_image():
    if 'image' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    # Retrieve the uploaded image file
    image = request.files['image']
    blob_name = image.filename

    # Step 1: Upload the image to Azure Blob Storage
    upload_to_blob_storage(image, blob_name)
    
    # Reset the file pointer after uploading to Blob Storage
    image.seek(0)

    # Step 2: Send the image to Custom Vision for analysis
    headers = {
        "Content-Type": "application/octet-stream",
        "Prediction-Key": PREDICTION_KEY
    }
    response = requests.post(PREDICTION_ENDPOINT, headers=headers, data=image.read())
    predictions = response.json().get("predictions", [])

    # Step 3: Return only predictions to the frontend
    return jsonify({"predictions": predictions})

if __name__ == '__main__':
    app.run(debug=True)
