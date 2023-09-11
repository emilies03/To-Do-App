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