// Global setting for terraform
terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "3.5.0"
    }
    aws = {
      source = "hashicorp/aws"
      version = "3.5.0"
    }
    kubernetes = {
      source = "hashicorp/kubernetes"
      version = "2.0.2"
    }
  }
}

// Provider block
provider "google" {
  credentials = file("<NAME>.json")
  project = "<PROJECT_ID>"
  region = "us-central1"
  zone = "us-central1-a"
}

provider "aws" {
  version = "~> 3.0"
  region = "us-west-2"
}

provider "kubernetes" {
  config_path = "~/.kube/config"
  config_context_auth_info = "ops"
  config_context_cluster = "mycluster"
}

// Resource block: Create actual cloud infrastructure
// Create a VPC
resource "aws_vpc" "example" {
  cidr_block = "10.0.0.0/16"
}

resource "kubernetes_namespace" "example" {
  metadata {
    name = "example"
  }
}

// Resource type: "google_compute_instance"
// Resource name: "vm_instance
resource "google_compute_instance" "vm_instance" {
  name = "JW Instance" // Name of the VM
  machine_type = "e2-micro"
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }
  network_interface {
    network = "default"
    access_config {
      // Include this section to give the VM an external IP address
    }
  }
}

// VPC
resource "google_compute_network" "vpc_network" {
  name = "terraform-network"
}
```