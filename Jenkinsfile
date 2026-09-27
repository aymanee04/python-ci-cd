pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/aymanee04/python-ci-cd.git'
            }
        }

        stage('Test') {
            steps {
                echo 'Projet récupéré avec succès !'
            }
        }
    }
}