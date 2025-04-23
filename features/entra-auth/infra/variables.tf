variable "tenant_id" {
  type        = string
  description = "Azure AD tenant ID"
}

variable "app_display_name" {
  type        = string
  description = "Name of the App Registration"
  default     = "openai-secure-chatbot"
}
