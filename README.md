# Azure OpenAI Secure Chatbot

A minimal Python-based chatbot using Azure OpenAI, secured via environment variables and deployable with Terraform.

## 🔧 Features
- Flask API with single `/chat` endpoint
- Uses Azure OpenAI `gpt-35-turbo` deployment
- `.env` based config for easy secrets management
- Terraform script for resource provisioning

## 🚀 Quickstart

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/azure-openai-secure-chatbot.git
cd azure-openai-secure-chatbot
```

### 2. Set up the Python environment
```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
```bash
cp app/.env.example app/.env
# Then edit .env and add your Azure OpenAI endpoint, key, and deployment name
```

### 5. Run the Flask app locally
```bash
python app/main.py
```

### 6. Test the endpoint
```bash
curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"prompt": "Tell me a joke."}'
```

### 7. Deploy Azure infrastructure with Terraform
```bash
cd infra
terraform init
terraform apply
```

## 📄 Related Blog Post
See full walkthrough here: [How I Built a Minimal Azure OpenAI Chatbot Using Flask, Terraform and GPT-4o](https://medium.com/@fhennek/how-i-built-a-minimal-azure-openai-chatbot-using-flask-terraform-and-gpt-4o-250f37d28920)

## 📁 Structure
- `app/` – Flask app with Azure OpenAI call
- `infra/` – Terraform infrastructure
- `docs/` – Diagrams and architecture visuals


