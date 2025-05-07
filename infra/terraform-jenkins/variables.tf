variable "hcloud_token" {
  type      = string
  sensitive = true
  description = "Hetzner Cloud API token"
}

variable "ssh_key_name" {
  type        = string
  description = "Name of SSH key stored in Hetzner"
}
