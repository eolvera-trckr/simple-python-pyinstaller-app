pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                withPythonEnv('python3') {
                    sh 'python -m py_compile sources/add2vals.py sources/calc.py' 
                    stash(name: 'compiled-results', includes: 'sources/*.py*')
                }
            }
        }
    }
}
