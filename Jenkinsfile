pipeline {
    agent any
    options { timestamps() }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Test (Unit tests)') {
            steps {
                // Запускаємо твій файл test.py всередині тимчасового контейнера python
                // Використовуємо %CD% для Windows, щоб підключити поточну папку
                bat '''
                docker run --rm ^
                  -v %CD%:/app ^
                  -w /app ^
                  python:3.11-slim ^
                  python test.py
                '''
            }
        }

        stage('Build & Push Docker Image') {
            steps {
                script {
                    def dockerHubUser = 'volodimirbabak'
                    def repoName = 'exam-app' 
                    
                    // УВАГА: Перевір, що ID в Jenkins (Credentials) точно такий самий: 'docker-hub-credentials'
                    // Якщо ти назвав їх 'dockerhub-creds', зміни назву в рядку нижче
                    docker.withRegistry('', 'docker-hub-credentials') {
                        
                        // Збірка образу
                        def image = docker.build("${dockerHubUser}/${repoName}:${env.BUILD_NUMBER}")
                        
                        // Відправка в DockerHub (версія з номером + latest)
                        image.push()
                        image.push('latest')
                    }
                }
            }
        }
    }

    post {
        success { echo "Всі етапи пройдено успішно! Образ завантажено." }
        failure { echo "Щось пішло не так. Перевір логи." }
        always { 
            // Очистка локальних образів, щоб не забивати місце
            bat 'docker rmi volodimirbabak/exam-app:%BUILD_NUMBER% || exit 0'
            bat 'docker rmi volodimirbabak/exam-app:latest || exit 0'
        }
    }
}