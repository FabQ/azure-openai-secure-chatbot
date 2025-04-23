output "client_id" {
  value = azuread_application.chatbot_app.application_id
}

output "client_secret" {
  value     = azuread_application_password.chatbot_secret.value
  sensitive = true
}
