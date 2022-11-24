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


resource "digitalocean_app" "app" {
  spec {
    name   = "pdfsvc-app"
    region = "sfo"
    env {
      key   = "APP_HOST"
      value = "$${APP_DOMAIN}"
      scope = "RUN_TIME"
      type  = "GENERAL"
    }
    env {
      key   = "DB_HOST"
      value = "$${db.PORT}"
      scope = "RUN_TIME"
      type  = "GENERAL"
    }
    env {
      key   = "DB_PORT"
      value = "$${db.PORT}"
      scope = "RUN_TIME"
      type  = "GENERAL"
    }
    env {
      key   = "DB_NAME"
      value = "$${db.DATABASE}"
      scope = "RUN_TIME"
      type  = "GENERAL"
    }
    env {
      key   = "DB_USER"
      value = "$${db.USERNAME}"
      scope = "RUN_TIME"
      type  = "GENERAL"
    }
    env {
      key   = "DB_PWD"
      value = "$${db.PASSWORD}"
      scope = "RUN_TIME"
      type  = "SECRET"
    }
    env {
      key   = "CELERY_BROKER_URL"
      value = cloudamqp_instance.instance.url
      scope = "RUN_TIME"
      type  = "SECRET"
    }
    service {
      name               = "pdfsvc-api"
      http_port          = 8000
      instance_count     = 1
      instance_size_slug = "basic-xs"
      image {
        registry_type = "DOCR"
        repository    = digitalocean_container_registry.registry.name
        tag           = "latest"
      }
      run_command = "unitd --no-daemon --control unix:/var/run/control.unit.sock"
    }
    worker {
      name               = "celery-worker"
      instance_size_slug = "basic-xs"
      instance_count     = 1
      image {
        registry_type = "DOCR"
        repository    = digitalocean_container_registry.registry.name
        tag           = "latest"
      }
      run_command = "celery -A pdfsvc worker --concurrency=5"
    }

    database {
      name       = "db"
      engine     = "PG"
      production = false
    }
  }
}
