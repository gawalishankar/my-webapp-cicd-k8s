My Web App CI/CD with Kubernetes

This repository demonstrates a complete CI/CD pipeline for a web application, utilizing GitHub Actions for Continuous Integration (CI), Docker for containerization, and Kubernetes for deployment. The pipeline automates the process of building, testing, and deploying the application, ensuring a streamlined and efficient workflow.

Architecture Overview

The architecture includes:

Frontend: A React.js application located in the frontend directory.

Backend: A Python Flask API located in the backend directory.

Docker: Dockerfiles for both frontend and backend to containerize the applications.

Kubernetes: Kubernetes manifests in the k8s directory for deploying the applications.

CI/CD Pipeline: GitHub Actions workflows defined in .github/workflows to automate the build and deployment processes.

Features

Automated Build and Test: GitHub Actions workflows automatically build and test the applications upon code changes.

Containerization: Both frontend and backend applications are containerized using Docker, ensuring consistency across environments.

Continuous Deployment: The pipeline deploys the applications to a Kubernetes cluster upon successful build and test.

Scalability: The Kubernetes deployment supports scaling the applications as needed.

Prerequisites

Before setting up the project, ensure you have the following:

Docker installed on your local machine.

Access to a Kubernetes cluster (e.g., Minikube, AKS, EKS).

kubectl configured to interact with your Kubernetes cluster.

GitHub repository with appropriate secrets configured for GitHub Actions.

Setup Instructions
1. Clone the Repository
git clone https://github.com/gawalishankar/my-webapp-cicd-k8s.git
cd my-webapp-cicd-k8s

2. Build Docker Images

Navigate to the frontend and backend directories and build the Docker images:

cd frontend
docker build -t my-frontend .
cd ../backend
docker build -t my-backend .

3. Push Docker Images to Registry

Tag and push the images to your preferred Docker registry:

docker tag my-frontend your-registry/my-frontend:latest
docker push your-registry/my-frontend:latest
docker tag my-backend your-registry/my-backend:latest
docker push your-registry/my-backend:latest

4. Deploy to Kubernetes

Apply the Kubernetes manifests to deploy the applications:

kubectl apply -f k8s/

5. Access the Applications

Expose the services to access the applications:

kubectl expose deployment frontend --type=LoadBalancer --name=frontend-service
kubectl expose deployment backend --type=LoadBalancer --name=backend-service


Retrieve the external IP addresses:

kubectl get svc


Access the frontend and backend applications using the external IPs provided.

GitHub Actions Workflows

The .github/workflows directory contains the following workflows:

CI Workflow: Triggered on push to the main branch. It builds and tests the applications.

CD Workflow: Triggered on successful completion of the CI workflow. It deploys the applications to the Kubernetes cluster.

Ensure that your GitHub repository has the necessary secrets configured for Docker registry authentication and Kubernetes access.

License

This project is licensed under the MIT License - see the LICENSE
 file for details.
