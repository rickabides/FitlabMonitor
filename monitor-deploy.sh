#!/bin/bash

# Build the Docker image and tag it
docker build -t monitorfitlab . && echo "Docker build successful." || { echo "Docker build failed."; exit 1; }

# Submit the Docker image to Google Cloud Build
gcloud builds submit --tag gcr.io/mlcclab-419521/monitorfitlab && echo "Cloud build successful." || { echo "Cloud build failed."; exit 1; }

# Deploy the Docker image on Google Cloud Run specifying the region
gcloud run deploy monitorfitlab --image gcr.io/mlcclab-419521/monitorfitlab --region us-central1 --allow-unauthenticated && echo "Deployment successful." || { echo "Deployment failed."; exit 1; }

echo "All operations completed successfully."

