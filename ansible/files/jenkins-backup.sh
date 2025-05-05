#!/bin/bash

# Папка за бекъпа
BACKUP_DIR="/var/backups/jenkins"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
DEST="$BACKUP_DIR/jenkins_backup_$TIMESTAMP.tar.gz"

# Jenkins Home – мястото, където Jenkins пази всичко
JENKINS_HOME="/var/lib/jenkins"

# Създаване на директория, ако я няма
mkdir -p "$BACKUP_DIR"

# Създаване на tar.gz архив от важните директории
tar -czf "$DEST" \
    --exclude="$JENKINS_HOME/war" \
    --exclude="$JENKINS_HOME/logs" \
    --exclude="$JENKINS_HOME/cache" \
    "$JENKINS_HOME"

echo "Backup completed: $DEST"
