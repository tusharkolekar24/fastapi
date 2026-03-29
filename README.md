### 📌 Overview

This project is a **FastAPI-based web API** that is fully containerized using **Docker** and deployed on **Microsoft Azure Cloud**. It is built with scalability and cloud-native best practices in mind, enabling seamless deployment with CI/CD pipelines or manual Docker push to Azure Container Registry.
<img width="1820" height="862" alt="image" src="https://github.com/user-attachments/assets/6d35fe0b-4e27-40c7-aaa2-2258898f3cdf" />

---

### 🚀 Features

* ✅ FastAPI backend with high performance
* ✅ Fully containerized using Docker
* ✅ Cloud deployment on Azure (Azure App Service / Azure Container Instances)
* ✅ Automatic API documentation with Swagger UI and ReDoc
* ✅ Easy to scale and maintain

---

### 📂 Project Structure

```
project-root/
├── src/                # API source code and business logic
├── app.py              # FastAPI application entry point
├── dockerfile          # Docker configuration file
├── requirements.txt    # Python dependencies
├── .gitignore          # Files/folders excluded from version control
├── LICENSE             # Licensing information
└── README.md           # Project documentation (this file)
```

---

### ⚙️ Installation & Local Setup

#### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd <project-folder>
```

#### 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4️⃣ Run the FastAPI App

```bash
uvicorn app:app --reload
```

🌐 Visit the API at: `http://127.0.0.1:8000`
📄 Swagger Docs: `http://127.0.0.1:8000/docs`

---

### 🐳 Docker Deployment

#### 1️⃣ Build Docker Image

```bash
docker build -t fastapi-azure-app .
```

#### 2️⃣ Run the Docker Container Locally

```bash
docker run -p 8000:8000 fastapi-azure-app
```

---

### ☁️ Azure Deployment

#### 📦 Step 1: Tag & Push to Azure Container Registry (ACR)

```bash
docker tag fastapi-azure-app <azure_registry_name>.azurecr.io/fastapi-azure-app:v1
az acr login --name <azure_registry_name>
docker push <azure_registry_name>.azurecr.io/fastapi-azure-app:v1
```

#### 🌐 Step 2: Deploy on Azure App Service or Azure Container Instance

```bash
az webapp create \
  --resource-group <your-resource-group> \
  --plan <app-service-plan> \
  --name <your-app-name> \
  --deployment-container-image-name <azure_registry_name>.azurecr.io/fastapi-azure-app:v1
```

---

### 📄 API Documentation

FastAPI automatically generates interactive docs:

* **Swagger UI:** `/docs`
* **ReDoc:** `/redoc`

---

### 🔐 Environment Variables (Optional)

Create `.env` file for secrets:

```
SECRET_KEY=your_secret
DATABASE_URL=your_database_connection
```

Load in code using `python-dotenv`.

---

### ✅ Requirements

* Python 3.8+
* FastAPI
* Uvicorn
* Docker
* Azure CLI

---

### 📌 Future Enhancements

* ➕ Add CI/CD with GitHub Actions or Azure DevOps
* 🌍 Add HTTPS and custom domain
* 📊 Integrate Azure Monitor for logging

---

### 🤝 Contribution

1. Fork the repo
2. Create feature branch
3. Submit pull request

---

### 📧 Contact

If you have questions or feedback, feel free to reach out or open an issue in the repository.

> ⭐ If you found this project useful, please star the repository!
