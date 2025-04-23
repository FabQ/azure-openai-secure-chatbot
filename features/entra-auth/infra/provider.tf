terraform {
  required_providers {
    azuread = {
      source  = "hashicorp/azuread"
      version = "~> 2.44"
    }
  }
}

provider "azuread" {
  tenant_id = var.tenant_id
}
