variable "prefix" {
  description = "The prefix used for all resources in this environment"
  default = "test"
}

variable "secret_key" {
  description = "The variable which is used to encrypt the flask session cookie"
  sensitive = true
}