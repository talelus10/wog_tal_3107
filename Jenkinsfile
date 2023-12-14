pipeline {
    agent any
    environment {
        DOCKER_COMPOSE_VERSION = '1.26.0'
        DOCKER_IMAGE_NAME = 'talelus10/tal_wog:latest
    }

    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Checkout to the git repo') {
            steps {
                checkout scm
            }
        }

        stage('Download docker compose') {
            steps {
                script {
                    bat "curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-Windows-x86_64.exe -o C:\\docker-compose.exe"
                }
            }
        }

        stage('Build the docker compose') {
            steps {
                script {
                    bat 'docker-compose build'
                }
            }
        }

        stage('Run the docker compose') {
            steps {
                script {
                    bat 'docker-compose up -d'
                }
            }
        }

        stage('Test the score with selenium') {
            steps {
                script {
                    bat 'pip install --no-cache-dir -r requirements.txt'
                    bat 'python e2e.py'
                }
            }
        }
        stage('Terminate the docker compose') {
            steps {
                script {
                    bat 'docker-compose down'
                }
            }
        }

        stage('Log in to DockerHub') {
            steps {
                script {
                    bat 'docker login -u="talelus10" -p="Maya2009!"'
                }
            }
        }

        stage('Push the New Image to DockerHub') {
            steps {
                script {
                    bat 'docker-compose push'
                }
            }
        }

    }
}
