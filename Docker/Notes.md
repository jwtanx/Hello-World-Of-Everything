# DOCKER BASICS

# Method 1: Dockerfile
```yaml
FROM python3.6

RUN mkdir -p /opt/project
COPY . /opt/project

WORKDIR /opt/project

EXPOSE 8080
CMD python run.py

```

# Method 2: Docker compose
1. Creating a docker-compose.yaml / docker-compose.yml file, both are the same. Make sure the name of the file is exactly docker-compose
```yaml
# The version for the docker-compo
version: "2.4"

services:
  mongodb:
    image: mongo:5.0.9
    container_name: pif-mongo
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: admin
    ports:
      - 27017:27017
    volumes:
      - ./data/db:/data/db
```

```bash
# New version
docker compose up

# Old version (Deprecated)
docker-compose up
```
---

## DIFFERENCE BETWEEN DOCKER IMAGE AND DOCKER CONTAINER
Docker image is like the game disk you put into your PC, the disk is built by somebody or even yourself
Docker container is made after your run the docker image (disk), you must run it and only run it for the first time using `docker run docker-image-name`. After you run it, a docker container is made (program is installed) then for the following time when you play the program, you have to start it by `docker start container-name` rather than running (installing) it again, unless you want to install it for another container.

## OVERALL IDEA FROM BUILDING IMAGE TO RUNNING IMAGE AND START IT
```bash
# Step 1: Start the docker first

# Step 2: Building the docker image with the dockerfile (-t to add a tag to it)
docker build -t docker-image:0.1 .
# A period is a must, indicating that you are getting the dockerfile in the current path as shown in the terminal
# The :0.1 is optional, without it, the version will be "latest"

# Checking the list of docker image to see if you have built the images
docker image ls

##### TO RUN THE IMAGE (THE "CD" YOU HAVE JUST BUILT) CREATE + START #####
docker run -it --name docker-container docker-image:0.1
# Always remember the docker-image name must be in the last parameter
# i: interactive and t: sudo terminal
# if you have include the version in the build process just now, this time you MUST include it too
# if you didnt put any version, just type docker-image is enough

##### TO SEE THE RUNNING DOCKER CONTAINER #####

##### STOPPING THE CONTAINER ####
docker stop docker-name

##### SECOND OR FOLLOWING TIME FOR EXECUTIION : MORE ADVANCED PARAMETERS AT THE BOTTOM #####
docker start docker-container
```

## GETTING THE LIST OF DOCKERS CONTAINER
```bash
# List out all the running docker containers
docker ps

# Listing all the docker containers that are running and not running
docker ps -a
```

## RUNNING THE DOCKER IMAGE
Once you have built the CD (docker image), you should run it first, it is like a disk, where you insert it, there is a game within it, and you have to click run to run the disk
```bash
# METHOD 1: USING THE HASH OF THE DOCKER IMAGE
docker run 4ed769366c2e

# METHOD 2: USING THE NAME OF THE DOCKER IMAGE
docker run docker-image

docker run -itd --name docker-name --publish 8080:8899 docker-image
# i: interactive
# t: terminal
# d: detached mode (running in the background)
# 8080 is the port exposed for the local host to connect whereas 8899 is the port internally in the docker

docker run -it --name docker-name --volume="%cd%/package/config":/package/config docker-image-name
docker run -it --name docker-name --volume="$(PWD7)/package/config":/package/config docker-image-name
# volume: binding the local files / folders with the folder inside of the container, when there is an update on the internal container / outside in the local machine, the files and folders will be synchronized.

# RUNNING THE DOCKER IMAGE IN THE BACKGROUND AND REMOVE IT AFTER WE ARE DONE
docker run --rm -itd -p 8080:80 <image-name>:<image-tag>
# rm: Remove the docker container once the docker container run everything it should be

```

## Starting the docker container (RUN THIS FOR SECOND OR CONSEQUTIVE TIME OR ELSE THE CONTAINER WILL BE CORRUPTED IF YOU USE DOCKER START)
```bash
docker start 4ed769366c2e
docker start docker-container
```

## Change into interactive mode for docker that is running
```bash
docker exec -it 4ed769366c2e sh
docker exec -it container_name sh
```

## Remove the docker container
```bash
docker rm container_name
```

## Remove the docker image
```bash
docker rmi image_name:0.1
docker image remove image_name:0.1
# `:0.1` is required if yoiu put a tag for it before
```

## MISC FUNCTION
```bash
docker restart discourse_app
docker stop discourse_app
docker start discourse_app -i (for interactive)
docker start discourse_app -itd (combination of interactive terminal and detached)
docker rename discourse_app disc_app
```

---

## REBUILDING IMAGES USING THE LATEST DOCKER CONTAINER
https://vsupalov.com/rebuilding-docker-image-development/

### Method 1: Using volume binding
1. Creating a docker-compose.yaml and bind the volume
```yaml
version: '3'
services:
  example:
    image: bash:4.4
    volumes:
      - ./package:/package # This method (./) will be taking the current directory, easier than the method of docker run --volume way
    # command: touch /app/target_dir/hello
````

2. Make some changes on the local machine in the package folder

3. Commmit the old container to a new image
```bash
docker commit old_container_name new_image_name
```

### Method 2: Using docker copy
1. Stop the container you are about to change

2. Copy the files on the local into the container path
```bash
docker cp main.py docker-container-name:app/package/path/main.py
```

3. Commmit the old container to a new image
```bash
docker commit old_container_name new_image_name
```

---

## STOPPING & REMOVING ALL THE DOCKER CONTAINER THEN REMOVE ALL THE IMAGES
```bash
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker rmi $(docker images)
```

---

## GETTING THE LIST OF THE INFORMATION OF THE DOCKER
```bash
docker info

# ...
# Storage Driver: overlay2
# ...
# Docker Root Dir: /var/lib/docker

```
Note: The data is stored under /var/lib/docker/overlay2

## CHECKING THE LIST OF THE LAYERS CREATED FOR THE IMAGE
```bash
docker history <image-name>

# 92ae8f82bc21 <----- The most top layer which is our layer (our image sha256)
# ...
# ...
# 09aa2ecd109d <----- The image we are building on top of (base image)
# <missing>
# <missing>
# <missing>

```

## CONTROL GROUPS - CGROUP
- Control groups is a feature of the Linux kernel.
- It allows us to limit the access processes and containers have to system resources such as CPU, RAM, IOPS, and network.
- We can enforce limits and constraints on docker containers too.
- A common use case is to limit the PIDs to prevent fork bombs.

- Finding the C group entries accociated with the docker containter
```bash
find /sys/fs/cgroup/ -name "6ef665788c2eb3b7b55e121ecb942c79e427383ed7622d3ca906bOfc2bbe782"
# Where "6ef665788c2eb3b7b55e121ecb942c79e427383ed7622d3ca906bOfc2bbe782" is the sha256 of the image
```
You will see a list of entries like pids, hugetlb, devices, freezer, cpu, net_cls, systemd, ... directory
Say, if we want to check the pids, we just cd to that path
`cd /sys/fs/cgroup/pids/6ef665788c2eb3b7b55e121ecb942c79e427383ed7622d3ca906bOfc2bbe782`

## STARTING THE DOCKER IN A USER REMAP WHERE THE ROOT IN THE DOCKER CANNOT ACCESS THE ROOT CONTENT ON THE HOST
```sudo dockerd --userns-remap=default &```

🤖 ChatGPT
| Terms                  | Explanation                                                                                                                                                                                                                                             |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dockerd                | To start the Docker daemon. The Docker daemon is responsible for managing and running Docker containers on your system.                                                                                                                                 |
| --userns-remap=default | This flag specifies that user namespace remapping should be enabled, with the default configuration. User namespace remapping is a security feature that helps isolate the permissions of containers from the host system.                              |
| &                      | The ampersand symbol at the end of the command puts the command in the background, allowing you to continue using the terminal without waiting for the command to complete. This is useful when starting long-running processes like the Docker daemon. |

By running this command, the Docker daemon will be started with user namespace remapping enabled using the default configuration.

```docker run -it --rm -v /:/shared/ alphine sh```
Although the root is shared and the user in docker is root, the host root directory is still not accessible