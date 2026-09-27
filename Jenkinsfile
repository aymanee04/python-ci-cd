pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'TON_URL_GITHUB'
            }
        }

        stage('Test') {
            steps {
                echo 'Projet récupéré avec succès !'
            }
        }
    }
}