# Entra ID Authenticated Chatbot (Flask + Azure OpenAI)

This version of the chatbot adds Entra ID (Azure AD) authentication to the `/chat` endpoint.

## 🚀 How to Run

1. Set up an App Registration in Entra ID
2. Configure `.env` with the following values:
   - `AZURE_TENANT_ID`
   - `AZURE_CLIENT_ID`
   - `AZURE_OPENAI_KEY`, etc.
3. Run the app:

```bash
pip install -r requirements.txt
python main.py
```

Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser and authenticate to use the web UI.
