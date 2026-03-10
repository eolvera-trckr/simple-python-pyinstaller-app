pipeline {
    agent {
        kubernetes {
            yamlFile 'k8s-build-pod.yml'
        }
    }
    environment {
        REPO_NAME = "${env.JOB_NAME.split('/')[-1]}"
    }
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                container('python') {
                    sh 'python3 -m py_compile sources/add2vals.py sources/calc.py'
                    stash(name: 'compiled-results', includes: 'sources/*.py*')
                }
            }
        }
        stage('Test') {
            steps {
                container('python') {
                    sh 'python3 -m pytest --junit-xml test-reports/results.xml sources/test_calc.py'
                }
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Snyk Code Scan') {
            steps {
                container('snyk') {
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
        }
        stage('Deliver') {
            steps {
                container('python') {
                    sh 'python3 -m PyInstaller --onefile sources/add2vals.py'
                }
            }
            post {
                success {
                    archiveArtifacts 'dist/add2vals'
                }
            }
        }
    }
}   
