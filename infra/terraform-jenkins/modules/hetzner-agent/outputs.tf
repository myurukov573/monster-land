output "ipv4_address" {
  value       = hcloud_server.agent.ipv4_address
  description = "Публичният IPv4 адрес на сървъра"
}

output "name" {
  value       = hcloud_server.agent.name
  description = "Името на създадения сървър"
}
