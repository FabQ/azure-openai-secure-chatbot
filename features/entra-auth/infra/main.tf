resource "azuread_application" "chatbot_app" {
  display_name = var.app_display_name
  sign_in_audience = "AzureADMyOrg"
  web {
    redirect_uris = ["http://localhost:5000"]
  }
}

resource "azuread_service_principal" "chatbot_sp" {
  application_id = azuread_application.chatbot_app.application_id
}

resource "azuread_application_password" "chatbot_secret" {
  application_object_id = azuread_application.chatbot_app.id
  display_name          = "chatbot-client-secret"
  end_date_relative     = "8760h" # 1 year
}
