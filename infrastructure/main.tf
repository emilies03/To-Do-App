terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = ">= 3.8"
    }
  }
   backend "azurerm" {
      resource_group_name  = "Cohort25_EmiSto_ProjectExercise"
      storage_account_name = "tfstateemtodoapp"
      container_name       = "tfstate"
      key                  = "terraform.tfstate"
  }
}

provider "azurerm" {
  features {}
}

data "azurerm_resource_group" "main" {
  name     = "Cohort25_EmiSto_ProjectExercise"
}

resource "azurerm_service_plan" "main" {
  name                = "terraformed-asp"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  os_type             = "Linux"
  sku_name            = "B1"
}

resource "azurerm_linux_web_app" "main" {
  name                = "${var.prefix}-em-todoapp"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  service_plan_id     = azurerm_service_plan.main.id

  site_config {
    application_stack {
      docker_image_name   = "emilie03/todo-app:main"
      docker_registry_url = "https://index.docker.io"
    }
  }

  app_settings = {
    SECRET_KEY                   = "PLACEHOLDER"
    PRIMARY_DB_CONNECTION_STRING = azurerm_cosmosdb_account.main.connection_strings[0]
    DATABASE_NAME                = azurerm_cosmosdb_mongo_database.main.name
  }

  lifecycle { ignore_changes = [ app_settings["SECRET_KEY"] ] }
}

resource "azurerm_cosmosdb_account" "main" {
  name                = "${var.prefix}-em-todoapp-db"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  offer_type          = "Standard"
  kind                = "MongoDB"

  # lifecycle { prevent_destroy = true }
  
  capabilities {
    name = "EnableServerless"
  }

  capabilities {
    name = "EnableAggregationPipeline"
  }

  capabilities {
    name = "mongoEnableDocLevelTTL"
  }

  capabilities {
    name = "MongoDBv3.4"
  }

  capabilities {
    name = "EnableMongo"
  }

  consistency_policy {
    consistency_level = "Session"
  }

  geo_location {
    location          = "westus"
    failover_priority = 0
  }
}

resource "azurerm_cosmosdb_mongo_database" "main" {
  name                = "ToDoAppDatabase"
  resource_group_name = azurerm_cosmosdb_account.main.resource_group_name
  account_name        = azurerm_cosmosdb_account.main.name
}