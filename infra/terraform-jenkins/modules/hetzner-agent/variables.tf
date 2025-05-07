variable "name" {
  type        = string
  description = "Името на сървъра"
}

variable "ssh_key_name" {
  type        = string
  description = "Името на SSH ключа в Hetzner"
}

variable "labels" {
  type        = list(string)
  description = "Списък със етикети за сървъра"
}

variable "user_data" {
  type        = string
  description = "Cloud-init скрипт за начална настройка"
}
