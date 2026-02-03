library 'status-jenkins-lib@v1.9.10'

pipeline {
  agent {
    docker {
      label 'linuxcontainer'
      image 'harbor.status.im/infra/ci-build-containers:linux-base-1.0.0'
      args '--volume=/nix:/nix ' +
           '--volume=/etc/nix:/etc/nix ' +
           '--user jenkins'
    }
  }

  options {
    timestamps()
    /* Prevent Jenkins jobs from running forever */
    timeout(time: 10, unit: 'MINUTES')
    /* manage how many builds we keep */
    buildDiscarder(logRotator(
      numToKeepStr: '20',
      daysToKeepStr: '30',
    ))
    disableConcurrentBuilds()
  }

  environment {
    GIT_COMMITTER_NAME = 'status-im-auto'
    GIT_COMMITTER_EMAIL = 'auto@status.im'
  }

  stages {
    stage('Deps') {
      steps { script {
        nix.develop('npm install --ignore-scripts=false')
      } }
    }

    stage('Build') {
      steps { script {
        nix.develop('npx quartz build')
        jenkins.genBuildMetaJSON('public/build.json')
      } }
    }

    stage('Publish Prod') {
      steps { script {
        sshagent(credentials: ['status-im-auto-ssh']) {
          nix.develop('ghp-import -c ecosystem.logos.co -p public', pure: false)
        }
      } }
    }
  }
}
