output "jenkins_agent_01_ip" {
  value       = module.jenkins-agent-01.ipv4_address
  description = "IPv4 адрес на jenkins-agent-01"
}

output "jenkins_agent_02_ip" {
  value       = module.jenkins-agent-02.ipv4_address
  description = "IPv4 адрес на jenkins-agent-02"
}
