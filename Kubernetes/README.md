# Kubernetes

ChatGPT: https://chat.openai.com/share/f9edbb11-4fab-47e5-91b3-c427d44a4653

## Installation
### Ubuntu
Reference: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
1. Check the CPU architecture of your PC
```bash
uname -m
# x86-64 or ARM64
```
- Download according to the type
```bash
# x86-64
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
```
```bash
# ARM64
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl"
```
- You can also download the specific version, for example: `v1.27.4`
```bash
curl -LO "https://dl.k8s.io/release/v1.27.4/bin/linux/amd64/kubectl"
```

- Optional: Validate the checksum
```bash
# x86-64
curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
# kubectl: OK
# If there is an error, just make sure the version you are installing for both binary file is the same version
```

- Installing kubectl with the binary file you have downloaded
```bash
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```
- If you do not have root access
```bash
chmod +x kubectl
mkdir -p ~/.local/bin
mv ./kubectl ~/.local/bin/kubectl

# Append (or prepend) ~/.local/bin to $PATH
nano ~/.bashrc

# Scroll to the end of the file and add the following line:
export PATH=$PATH:~/.local/bin

```

- Check installation completion
```bash
kubectl version --client
# If there is error, make sure you are installing the correct CPU's architecture
```

### Windows
Check the guide here: https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/

## References
Documentation: https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands
Cheat Sheet: https://kubernetes.io/docs/reference/kubectl/cheatsheet/

## Most frequently used commands
### Cluster
| Commands               | Description                             |
| ---------------------- | --------------------------------------- |
| `kubectl cluster-info` | Display cluster information             |
| `kubectl get nodes`    | View the available nodes in the cluster |

### Namespace
| Commands                                  | Description                        |
| ----------------------------------------- | ---------------------------------- |
| `kubectl get namespaces`                  | View all namespaces in the cluster |
| `kubectl create namespace NAMESPACE_NAME` | Create a new namespace             |

### Deployment
| Commands                                                           | Description                                   |
| ------------------------------------------------------------------ | --------------------------------------------- |
| `kubectl get deployments `                                         | View all deployments in the current namespace |
| `kubectl create deployment DEPLOYMENT_NAME --image=IMAGE_NAME:TAG` | Create a new deployment                       |

### Pod
| Commands                        | Description                                    |
| ------------------------------- | ---------------------------------------------- |
| `kubectl get pods`              | View all pods in the current namespace         |
| `kubectl describe pod POD_NAME` | View detailed information about a specific pod |
| `kubectl logs POD_NAME`         | View logs for a specific pod                   |

### Services
| Commands                                                                            | Description                                |
| ----------------------------------------------------------------------------------- | ------------------------------------------ |
| `kubectl expose deployment DEPLOYMENT_NAME --port=SERVICE_PORT --type=SERVICE_TYPE` | Expose a deployment as a service           |
| `kubectl get services`                                                              | View all services in the current namespace |
| `kubectl delete service SERVICE_NAME`                                               | Delete a service                           |

### Scaling
| Commands                                                          | Description                                               |
| ----------------------------------------------------------------- | --------------------------------------------------------- |
| kubectl scale deployment DEPLOYMENT_NAME --replicas=REPLICA_COUNT | Scale the number of replicas for a deployment             |
| kubectl autoscale deployment DEPLOYMENT_NAME --min=2 --max=10     | Auto scale the deployment with replica of min 2 to max 10 |

### Updating Resources / Rolling Updates
| Commands                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| kubectl set image deployment DEPLOYMENT_NAME CONTAINER_NAME=NEW_IMAGE:TAG | Perform a rolling update by updating the container image for a deployment |
| kubectl rollout history deployment DEPLOYMENT_NAME                        | Check the history of deployments including the revision                   |
| kubectl rollout undo deployment DEPLOYMENT_NAME                           | Rollback to the previous deployment                                       |
| kubectl rollout undo deployment DEPLOYMENT_NAME --to-revision=2           | Rollback to a specific revision                                           |
| kubectl rollout status -w deployment DEPLOYMENT_NAME                      | Watch rolling update status of "frontend" deployment until completion     |
| kubectl rollout restart deployment DEPLOYMENT_NAME                        | Rolling restart of the "frontend" deployment                              |

### Port Forwarding
| Commands                                             | Description                                           |
| ---------------------------------------------------- | ----------------------------------------------------- |
| kubectl port-forward POD_NAME LOCAL_PORT:REMOTE_PORT | Forward a local port to a specific pod in the cluster |

### Deleting REsources
| Commands                                     | Description                                                |
| -------------------------------------------- | ---------------------------------------------------------- |
| kubectl delete deployment DEPLOYMENT_NAME    | Delete a deployment                                        |
| kubectl delete service SERVICE_NAME          | Delete a service                                           |
| kubectl delete -f ./pod.json                 | Delete a pod using the type and name specified in pod.json |
| kubectl delete pod unwanted --now            | Delete a pod with no grace period                          |
| kubectl delete pod,service baz foo           | Delete pods and services with same names "baz" and "foo"   |
| kubectl delete pods,services -l name=myLabel | Delete pods and services with label name=myLabel           |
| kubectl -n my-ns delete pod,svc --all        | Delete all pods and services in namespace my-ns,           |

## Other
`kubectl --namespace default port-forward <path/to/svc> 8080:8080 >> /dev/null & Port forwarding the service to a port number`
`kubectl get nodes --output wide`
`kubectl get nodes --output yaml | grep -A4 addresses`
`kubectl exec --namespace default -it svc/myjenkins -c jenkins -- /bin/cat /run/secrets/additional/chart-admin-password && echo`
`kubectl run -it --rm alpine --image=alpine:3.6 --restart=Never nslookup mycache-memcached.default.svc.cluster.local`

To confirm that the locust-master pod is created, run the following command:
`kubectl get pods -l app=locust-master`
`kubectl create deployment hello-server --image=gcr.io/google-samples/hello-app:1.0`
`kubectl expose deployment hello-server --name orca-hello-service --type LoadBalancer --port 80 --target-port 8080`

## Differences
| Left term                                                                                                              |      Comparison       | Right term                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------- | :-------------------: | ------------------------------------------------------------------------------------------------ |
| Concerned with defining the desired state of the application and ensuring the specified number of replicas are running | Deployment × Services | Focuses on defining how external or internal clients can access the pods running the application |

## Basic Scripts
### Service
```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
  type: ClusterIP
```
| Property   | Explanation                                                                                                                             |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `kind`     | Specifies the purpose of the yaml file                                                                                                  |
| `metadata` | Defines a Service named "my-service"                                                                                                    |
| `selector` | Is used to match the pods that the service should expose. In this example, it selects pods with the label "app: my-app"                 |
| `ports`    | Specifies the port configuration for the service. The service listens on port 80 and forwards traffic to the pods' port 8080            |
| `type`     | Determines the type of service. Here, it is set to "ClusterIP," which means the service will only be accessible from within the cluster |

### Deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
        - name: my-app-container
          image: my-app:latest
          ports:
            - containerPort: 8080
```
| Property     | Explanation                                                                                                                    |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `metadata`   | Defines a Deployment named "my-app-deployment"                                                                                 |
| `replicas`   | Specifies the desired number of replicas (pods) for the application, which is set to 3 in this example                         |
| `selector`   | Is used to match the pods controlled by the Deployment. It uses the label "app: my-app" to select the pods                     |
| `template`   | Defines the pod template that the Deployment will create. It includes the pod's metadata and the container specifications      |
| `containers` | Inside the pod template specifies the container named "my-app-container" based on the "nginx:latest" image, exposing port 8080 |

To be continue with virtual-service, config, kustomization for istio etc

## Installing minikube
https://minikube.sigs.k8s.io/docs/start/