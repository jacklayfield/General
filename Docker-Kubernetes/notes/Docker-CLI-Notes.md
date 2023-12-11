# Docker CLI

| Command                                                    | Description                                     |
| ---------------------------------------------------------- | ----------------------------------------------- |
| docker info                                                | Displays system information                     |
| docker version                                             | Displays system's version                       |
| docker login                                               | Logs in to Docker                               |
| docker pull [imageName]                                    | Pulls an image from a registry                  |
| docker run [imageName]                                     | Run containers                                  |
| docker run -d [imageName]                                  | Detached mode                                   |
| docker start [containerName]                               | Start stopped containers                        |
| docker ps                                                  | List running containers                         |
| docker ps -a                                               | List running and stopped containers             |
| docker stop [containerName]                                | Stop containers                                 |
| docker kill [containerName]                                | Kill containers                                 |
| docker image inspect [imageName]                           | Get image info                                  |
| docker run -it nginx -- /bin/bash                          | Attach shell                                    |
| docker run -it -- microsoft/powershell:nanoserver pwsh.exe | Attach PowerShell                               |
| docker container exec -it [containerName] -- bash          | Attach to a running container                   |
| docker rm [containerName]                                  | Removes stopped containers                      |
| docker rm $(docker ps -a -q)                               | Removes all stopped containers                  |
| docker images                                              | Lists images                                    |
| docker rmi [imageName]                                     | Deletes the image                               |
| docker system prune -a                                     | Removes all images not in use by any containers |
| docker create volume [volumeName]                          | Creates a new volume                            |
| docker volume ls                                           | Lists the volumes                               |
| docker volume inspect [volumeName]                         | Display volume info                             |
| docker volume rm [volumeName]                              | Deletes a volume                                |
| docker volume prune                                        | Deletes all volumes not mounted                 |
