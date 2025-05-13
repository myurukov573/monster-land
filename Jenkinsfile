pipeline {
    agent { label 'jenkins-agent-1' }

    environment {
        IMAGE_NAME = "ghcr.io/myurukov573/monster-land"
        TAG = "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/myurukov573/monster-land.git'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$TAG .'
            }
        }

        stage('Extract GHCR Token from Vault') {
            steps {
                dir('ansible') {
                    sh '''
                        echo "$VAULT_PASSWORD" > .vault_pass.txt
                        GHCR_TOKEN=$(ansible-vault view vault/vault.yml --vault-password-file .vault_pass.txt | grep ghcr_token | awk '{print $2}')
                        echo "GHCR_TOKEN=$GHCR_TOKEN" > ../ghcr.env
                        shred -u .vault_pass.txt
                    '''
                }
            }
        }

        stage('Push to GHCR') {
            steps {
                sh '''
                    source ghcr.env
                    echo $GHCR_TOKEN | docker login ghcr.io -u myurukov573 --password-stdin
                    docker push $IMAGE_NAME:$TAG
                '''
            }
        }

        stage('Deploy via Ansible') {
            steps {
                dir('ansible') {
                    sh '''
                        echo "$VAULT_PASSWORD" > .vault_pass.txt
                        ansible-playbook deploy.yml --vault-password-file .vault_pass.txt
                        shred -u .vault_pass.txt
                    '''
                }
            }
        }
    }

    post {
        always {
            sh 'rm -f ghcr.env'
            cleanWs()
        }
    }
}
