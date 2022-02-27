pipeline {
    agent any

    stages {

        stage('Get Source') {
            steps {
                echo 'Get Source ok....'
                git branch: 'master', url: 'https://github.com/ChrisMarSilva/cms-python-jenkins.git', credentialsId: 'github'
            }
        }

        stage ('Docker Build') {
            steps {
                echo 'Docker Build ok....'
                script {
                    dockerapp = docker.build("chrismarsilva/cms-python-jenkins:${env.BUILD_ID}", '-f ./Dockerfile ./')
                }
            }
        }

        stage ('Docker Push Image') {
            steps {
                echo 'Docker Push Image ok....'
                script {
//                     docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
//                         dockerapp.push('latest')
//                         dockerapp.push("${env.BUILD_ID}")
//                     }
                }
            }
        }

        stage('Build App') {
            steps {
                echo 'Build ok....'
            }
        }

        stage('Test App') {
            steps {
                echo 'Test ok....'
            }
        }

        stage('Deploy App') {
            steps {
                echo 'Deploying ok....'
            }
        }

    }
}

/*



// cms-python-jenkins
// https://github.com/ChrisMarSilva/cms-python-jenkins.git

https://www.fourkitchens.com/blog/article/trigger-jenkins-builds-pushing-github/
https://www.blazemeter.com/blog/how-to-integrate-your-github-repository-to-your-jenkins-project

pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('build') {
            steps {
                echo 'Build Image ok2....'
                //sh 'python --version'
            }
        }
    }
}


pipeline {
    //agent any
    //agent { docker { image 'tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim' } }
    //agent { docker { image 'python3.9-slim' } }
    agent { docker { image 'python:3.10.1-alpine' } }
    //agent { docker { image 'python:3.7' label 'docker && linux' } }
    // agent { dockerfile { filename 'Dockerfile' } }
    // agent { docker { image 'python:3.9-slim-buster' } }


    stages {

        stage ('Build Image') {
            steps {
                echo 'Build Image ok2....'
//                 script {
//                     dockerapp = docker.build("chrismarsilva/cms-python-jenkins:${env.BUILD_ID}", '-f ./Dockerfile ./')
//                 }
            }
        }

        stage ('Push Image') {
            steps {
                echo 'Push Image ok....'
//                 script {
//                     docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
//                         dockerapp.push('latest')
//                         dockerapp.push("${env.BUILD_ID}")
//                     }
//                 }
            }
        }

        stage ('Deploy Kubernetes') {
            environment {
                tag_version = "${env.BUILD_ID}"
            }
            steps {
                echo 'Deploy Kubernetes ok....'
//                 withKubeConfig([credentialsId: 'kubeconfig']) {
//                     sh 'sed -i "s/{{tag}}/$tag_version/g" ./deployment.yaml'
//                     sh 'kubectl apply -f ./deployment.yaml'
//                 }
            }
        }

        stage('Build') {
//             withEnv(["HOME=${env.WORKSPACE}"]) {
//               sh "pip install -r requirements.txt --user"
//             }
            steps {
                echo 'Build ok....'
                sh 'python --version'
//                 sh 'python -V'
//                 sh 'python -m pip install --upgrade pip'
                //sh 'pip install --upgrade pip'
               // sh 'python -m pip install -r requirements.txt --user --no-cache'
                // sh 'python setup.py sdist'
//                 sh '''
//                     python -V
//                     sudo python -m pip install -r requirements.txt --user --no-cache
//                     sudo python setup.py sdist
//                 '''
            }
        }

        stage('Test') {
            steps {
                echo 'Test ok....'
                // sh 'python test_main.py'
                //sh 'pytest test_main.py'
//                 sh '''
//                     python -m venv .venv
//                     . .venv/bin/activate
//                     pip install -r requirements.txt
//                     pytest -v
//                 '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying ok....'
            }
        }

        stage ('Commit in prod branch') {
            steps {
                echo 'Commit ok....'
                //sh ''' echo "commit prod branch" '''
            }
        }

//         withCredentials([usernamePassword(credentialsId: 'ci-github', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
//         sh('git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/my-org/my-repo.git')
// }
//         stage('Update GIT') {
//           steps {
//             script {
//               catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
//                 withCredentials([usernamePassword(credentialsId: 'example-secure', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
//                     def encodedPassword = URLEncoder.encode("$GIT_PASSWORD",'UTF-8')
//                     sh "git config user.email admin@example.com"
//                     sh "git config user.name example"
//                     sh "git add ."
//                     sh "git commit -m 'Triggered Build: ${env.BUILD_NUMBER}'"
//                     sh "git push https://${GIT_USERNAME}:${encodedPassword}@github.com/${GIT_USERNAME}/example.git"
//                 }
//               }
//             }
//           }
//         }

    }
}

*/

