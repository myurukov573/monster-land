terraform {
  required_providers {
    hcloud = {
      source  = "hetznercloud/hcloud"
      version = "~> 1.44"
    }
  }

  required_version = ">= 1.1.0"
}

provider "hcloud" {
  token = var.hcloud_token
}

module "jenkins-agent-01" {
  source       = "./modules/hetzner-agent"
  name         = "jenkins-agent-01"
  ssh_key_name = var.ssh_key_name
  labels       = ["jenkins", "agent"]
  user_data    = file("${path.module}/cloud-init/base.yaml")

  providers = {
    hcloud = hcloud
  }
}

module "jenkins-agent-02" {
  source       = "./modules/hetzner-agent"
  name         = "jenkins-agent-02"
  ssh_key_name = var.ssh_key_name
  labels       = ["jenkins", "agent"]
  user_data    = file("${path.module}/cloud-init/base.yaml")

  providers = {
    hcloud = hcloud
  }
}
