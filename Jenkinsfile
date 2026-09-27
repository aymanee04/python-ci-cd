pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install --upgrade pip
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Start Application') {
            steps {
                sh '''
                    nohup ./venv/bin/python app/app.py > flask.log 2>&1 &
                    sleep 5
                    curl -f http://localhost:5000/api/health
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    ./venv/bin/pytest tests/ --junitxml=pytest-results.xml
                '''
            }

            post {
                always {
                    junit 'pytest-results.xml'
                }
            }
        }
        stage('API Tests - Postman') {
    steps {
        sh '''
            newman run postman/python-ci-cd.postman_collection.json \
                --reporters cli,junit \
                --reporter-junit-export newman-results.xml
        '''
    }

    post {
        always {
            junit 'newman-results.xml'
        }
    }
}
    }
}