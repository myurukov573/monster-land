terraform {
  required_providers {
    hcloud = {
      source = "hetznercloud/hcloud"
    }
  }
}

resource "hcloud_server" "agent" {
  name        = var.name
  image       = "ubuntu-22.04"
  server_type = "cx22"
  location    = "fsn1"
  ssh_keys    = [var.ssh_key_name]
  labels      = { for l in var.labels : l => true }
  user_data   = var.user_data
}
