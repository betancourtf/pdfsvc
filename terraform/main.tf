terraform {
  required_providers {
    cloudamqp = {
      source  = "cloudamqp/cloudamqp"
      version = "1.20.0"
    }
    digitalocean = {
      source  = "digitalocean/digitalocean"
      version = "2.24.0"
    }
  }
}

resource "cloudamqp_instance" "instance" {
  name   = "pdf-rabbitmq-test"
  plan   = "lemur"
  region = "amazon-web-services::us-east-1"
  tags   = ["terraform"]
}

resource "digitalocean_container_registry" "registry" {
  name                   = "pdfsvc-registry"
  region                 = "sfo3"
  subscription_tier_slug = "starter"
}

resource "digitalocean_container_registry_docker_credentials" "registry_credentials" {
  registry_name = "pdfsvc-registry"
  write         = true
  depends_on = [
    digitalocean_container_registry.registry
  ]
}
