pipeline {
    //agent any
    agent { docker { image 'tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim' } }

    stages {

        stage ('Build Image') {
            steps {
                echo 'Build Image ok....'
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
            steps {
                echo 'Build ok....'
                // sh 'python --version'
                // sh 'pip install -r requirements.txt --user'
                // sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Test ok....'
                //sh 'python test_main.py'
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
                sh ''' echo "commit prod branch" '''
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

/*


http://localhost:8080/updateCenter/
http://localhost:8080/cms-tnb-python-site-fastapi/


https://www.youtube.com/watch?v=O6y27_Ol25g
https://www.youtube.com/watch?v=PxdsFL4NDfM

https://www.fourkitchens.com/blog/article/trigger-jenkins-builds-pushing-github/
https://www.blazemeter.com/blog/how-to-integrate-your-github-repository-to-your-jenkins-project




*/