pipeline {
    agent { label 'python-agent' }
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Snyk Code Scan') {
/*
            agent {
                docker {
                    image 'snyk/snyk:python'
                    args '--platform=linux/amd64 -e SNYK_TOKEN'
                    reuseNode true
                    alwaysPull true
                }
            }
*/
            steps {
                withCredentials([string(credentialsId: 'snyk-token', variable: 'SNYK_TOKEN')]) {
                    sh '''
                    curl -L -o snyk https://static.snyk.io/cli/latest/snyk-linux
                    chmod +x snyk
                    sudo mv snyk /usr/local/bin/
                    '''
                    sh 'snyk auth $SNYK_TOKEN'
                    sh 'snyk code test --severity-threshold=medium'
                }
            }
        }
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
