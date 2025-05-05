pipeline {
    agent { label 'jenkins-agent-1' }

    environment {
        IMAGE_NAME = "ghcr.io/myurukov573/monster-land"
        TAG = "latest"
        GHCR_TOKEN = credentials('ghcr-token')
    }

    stages {
        stage('Say Hello') {
            steps {
                sh 'echo Hello from Jenkins Agent!'
            }
        }

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

        stage('Push to GHCR') {
            steps {
                script {
                    try {
                        sh '''
                            echo $GHCR_TOKEN | docker login ghcr.io -u myurukov573 --password-stdin
                            docker push $IMAGE_NAME:$TAG
                        '''
                    } catch (err) {
                        echo "⚠️ Docker push failed: ${err}"
                    }
                }
            }
        }

        stage('Install Ansible Collections') {
            steps {
                dir('ansible') {
                    sh 'test -f requirements.yml && ansible-galaxy collection install -r requirements.yml || echo "No Ansible requirements.yml found."'
                }
            }
        }

        stage('Add SSH Host Key') {
            steps {
                // Доверяваме се на SSH ключа на целевия хост
                sh 'ssh-keyscan 37.27.251.233 >> ~/.ssh/known_hosts'
            }
        }

        stage('Deploy via Ansible') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'jenkins-agent-ssh', keyFileVariable: 'SSH_KEY', usernameVariable: 'SSH_USER')]) {
                    dir('ansible') {
                        sh '''
                            mkdir -p ~/.ssh
                            cp $SSH_KEY ~/.ssh/jenkins_agent_key
                            chmod 600 ~/.ssh/jenkins_agent_key
                            ansible-playbook -i inventory.ini deploy.yml -e "ghcr_token=$GHCR_TOKEN"
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            echo "📦 Cleaning workspace..."
            cleanWs()
        }
        failure {
            echo "❌ Build failed!"
        }
        success {
            echo "✅ Deployment completed successfully!"
        }
    }
}
