terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.14.1"
    }
  }
}

provider "google" {
  credentials = "./keys/my_creds.json"
  project     = "terraform-learning-446910"
  region      = "europe-west9"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "terraform-learning-446910-terra-bucket"
  location      = "EU"
  force_destroy = true

  // Age is gonna be in days.

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}