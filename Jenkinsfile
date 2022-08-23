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

                    sh 'python3 -m venv .venv'
                    sh 'cd test_env/bin'
                    sh 'pwd'
                    sh 'ls -la'
                    sh 'source .venv/bin/activate'
                    sh 'pip install Django==3.1.5'
                    sh 'pip install pytz==2017.2'
                    sh 'pip install django-crispy-forms'
                    sh 'pip install djangorestframework'

            }
        }
        stage('Run Migrations'){
            steps{

                    sh 'python3 manage.py migrate'

            }
        }
    }
}