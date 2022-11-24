terraform {
  required_providers {
    cloudamqp = {
      source  = "cloudamqp/cloudamqp"
      version = "1.20.0"
    }
  }
}

resource "cloudamqp_instance" "instance" {
  name        = "pdf-rabbitmq-test"
  plan        = "lemur"
  region      = "amazon-web-services::us-east-1"
  tags        = ["terraform"]
}