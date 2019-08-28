pipeline{
    agent any
    stages{
        stage('checkout'){
            steps{
                git 'https://github.com/eldadtech/Second_Project.git'
            }
        }
		stage ('dockercompose')
		{
			steps{
				bat cd 'C:\\code\\DockerRedisPython'
				bat 'docker-compose up -d'
			}
			
		}
        stage ('build') {
            steps{
                bat 'python HelloWorld.py'
                
            }
        
        }
    }
}