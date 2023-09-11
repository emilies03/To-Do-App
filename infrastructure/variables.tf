variable "prefix" {
  description = "The prefix used for all resources in this environment"
  default = "test"
}

variable "loggly_token" {
  description = "Loggly token"
  sensitive = true
}

variable "log_level" {
  description = "Logging level"
  default = "WARNING"
}

variable "secret_key" {
  description = "The variable which is used to encrypt the flask session cookie"
  sensitive = true
}