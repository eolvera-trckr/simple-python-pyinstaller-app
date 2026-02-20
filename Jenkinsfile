pipeline {
    agent { label 'python-agent' }
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Snyk Code Scan') {
            steps {
                withCredentials([string(credentialsId: 'snyk-token', variable: 'SNYK_TOKEN')]) {
                    sh '''
                    # Authenticate
                    snyk auth $SNYK_TOKEN
                    # Scan dependencies
                    snyk test --severity-threshold=medium
                    # Scan code for security issues
                    snyk code test --severity-threshold=medium
                    '''
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
