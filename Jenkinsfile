pipeline {
    agent { label 'python-agent' }
    environment {
        REPO_NAME = "${env.JOB_NAME.split('/')[-1]}"
    }
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                sh 'python3 -m py_compile sources/add2vals.py sources/calc.py'
                stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest --junit-xml test-reports/results.xml sources/test_calc.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Snyk Code Scan') {
            agent {
                docker {
                    image 'snyk/snyk:alpine'
                    args '--entrypoint=""'
                }
            }
            steps {
                withCredentials([string(credentialsId: 'snyk-token', variable: 'SNYK_TOKEN')]) {
                    sh '''
                    # Authenticate
                    snyk auth $SNYK_TOKEN
                    # Scan dependencies
                    snyk test --all-projects --skip-unresolved --severity-threshold=medium || true
                    '''
                }
            }
        }
        stage('Deliver') {
            steps {
                sh 'python3 -m PyInstaller --onefile sources/add2vals.py'
            }
            post {
                success {
                    archiveArtifacts 'dist/add2vals'
                }
            }
        }
    }
}   
