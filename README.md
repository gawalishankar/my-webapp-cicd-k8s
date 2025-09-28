# 🚀 My Web App CI/CD with Kubernetes

This repository demonstrates a complete **CI/CD pipeline** for a web application, using **GitHub Actions** for CI, **Docker** for containerization, and **Kubernetes** for deployment. 🐳☸️

## 🏗 Architecture Overview

* **Frontend**: React.js application in the `frontend` directory. ⚛️
* **Backend**: Python Flask API in the `backend` directory. 🐍
* **Docker**: Dockerfiles for frontend and backend. 🐳
* **Kubernetes**: Manifests in the `k8s` directory. ☸️
* **CI/CD**: GitHub Actions workflows in `.github/workflows`. ⚙️

![CI/CD Pipeline](images/cicd_pipeline.png)

## ✨ Features

* ✅ Automated build and test with GitHub Actions.
* 🐳 Containerization for consistent environments.
* ☸️ Continuous deployment to Kubernetes.
* 📈 Scalable deployments using Kubernetes.

## ⚙️ Prerequisites

* Docker installed 🐳
* Kubernetes cluster (Minikube, AKS, or EKS) ☸️
* kubectl configured 🖥️
* GitHub repository with secrets for Docker registry and Kubernetes 🔐

## 🛠 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/gawalishankar/my-webapp-cicd-k8s.git
cd my-webapp-cicd-k8s
```

### 2️⃣ Build Docker Images

```bash
cd frontend
docker build -t my-frontend .
cd ../backend
docker build -t my-backend .
```

### 3️⃣ Push Docker Images

```bash
docker tag my-frontend your-registry/my-frontend:latest
docker push your-registry/my-frontend:latest

docker tag my-backend your-registry/my-backend:latest
docker push your-registry/my-backend:latest
```

### 4️⃣ Deploy to Kubernetes

```bash
kubectl apply -f k8s/
```

### 5️⃣ Access Applications

```bash
kubectl expose deployment frontend --type=LoadBalancer --name=frontend-service
kubectl expose deployment backend --type=LoadBalancer --name=backend-service
kubectl get svc
```

## ⚡ GitHub Actions Workflows

* **CI Workflow**: Builds and tests applications on push. 🧪
* **CD Workflow**: Deploys applications to Kubernetes on CI success. 🚀

## 📄 License

MIT License
