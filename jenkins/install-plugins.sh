#!/bin/bash

set -e

# Проверка дали Jenkins CLI съществува
if ! command -v jenkins-plugin-cli &> /dev/null; then
  echo "jenkins-plugin-cli not found. Install Jenkins >=2.222.1 or use Docker image with CLI."
  exit 1
fi

# Инсталира плъгините от plugins.txt
while read plugin || [[ -n "$plugin" ]]; do
  echo "Installing plugin: $plugin"
  jenkins-plugin-cli --plugins "$plugin"
done < plugins.txt
