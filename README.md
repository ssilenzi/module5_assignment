# module5_assignment: particle filter

## Commit rules

Please, commit into separate branches. In this way we can diff and merge our work.

    git checkout -b yourname
    git push -u origin yourname

## Tools

https://gitforwindows.org/ (Windows only)

https://github.com/magicmonty/bash-git-prompt (Linux only)

https://www.syntevo.com/smartgit/ (Windows and Linux)

## Credential managers

### Windows

To login into GitHub from Git Bash, you can setuo the Credential Manager during the setup of Git for Windows:

![cred_manager](https://user-images.githubusercontent.com/44733864/208418849-3b2c062e-eb91-4a23-984c-b8bc1bf8cda0.png)

### Linux

Here is a bit more complex, but not so much:

    wget https://github.com/GitCredentialManager/git-credential-manager/releases/download/v2.0.886/gcm-linux_amd64.2.0.886.deb
    sudo apt-get update
    sudo apt-get install -y ./gcm-linux_amd64.2.0.886.deb
    rm -f gcm-linux_amd64.2.0.886.deb
    git-credential-manager configure
