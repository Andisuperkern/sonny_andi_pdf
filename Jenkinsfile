pipeline{
    agent any

    stages{
        stage('Compile Stage'){
            steps{

                    sh 'ls -la'

            }
        }
        stage('Pip install'){
            steps{

                    sh 'pip install Django'
                    sh 'pip install django-crispy-forms'
                    sh 'pip install djangorestframework'

            }
        }
        stage('Run Migrations'){
            steps{

                    sh 'python3 manage.py migrate'

            }
        }
        stage('Unit Testing'){
            steps{

                    sh 'python3 manage.py test sonny_andi_pdf'

            }
        }
        stage('Docker Deploy'){
            steps{
                    sh 'ls'
                    dir('./docker_launch_files'){
                        sh 'ls'
                        sh 'docker compose down'
                        sh 'docker compose build'
                        sh 'docker compose up --detach'
                    }

            }
        }
    }
}