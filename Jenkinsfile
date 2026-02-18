pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                withPythonEnv('python3') {
                    sh 'python3 -m py_compile sources/add2vals.py sources/calc.py'
                    stash(name: 'compiled-results', includes: 'sources/*.py*')
                }
            }
        }
        stage('Test') {
            steps {
                withPythonEnv('python3') {
                    sh 'pip install pytest'
                    sh 'py.test --junit-xml test-reports/results.xml sources/test_calc.py'
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Deliver') {
            steps {
                withPythonEnv('python3') {
                    sh 'pip install pyinstaller'
                    sh 'pyinstaller --onefile sources/add2vals.py'
                    archiveArtifacts 'dist/add2vals'
                }
            }
        }
    }
}   
