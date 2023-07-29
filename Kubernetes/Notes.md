# Kubernetes Cheat Sheet

| Commands                                                                        | Description                                                                  |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| kubectl cluster-info                                                            | Confirm that you can connect to your cluster                                 |
| kubectl get pods                                                                | Check the rediness, status and the age of the pods                           |
| kubectl --namespace default port-forward <path/to/svc> 8080:8080 >> /dev/null & | Port forwarding the service to a port number                                 |
| kubectl get svc                                                                 | Get the list of services (NAME, TYPE, CLUSTER-IP, EXTERNAL-IP, PORT(S), AGE) |


sudo apt-get install kubectl
kubectl get nodes --output yaml | grep -A4 addresses
kubectl get nodes --output wide

## Other
kubectl exec --namespace default -it svc/myjenkins -c jenkins -- /bin/cat /run/secrets/additional/chart-admin-password && echo
kubectl run -it --rm alpine --image=alpine:3.6 --restart=Never nslookup mycache-memcached.default.svc.cluster.local

To confirm that the locust-master pod is created, run the following command:
kubectl get pods -l app=locust-master

kubectl scale deployment/locust-worker --replicas=20
kubectl create deployment hello-server --image=gcr.io/google-samples/hello-app:1.0
kubectl expose deployment hello-server --name orca-hello-service --type LoadBalancer --port 80 --target-port 8080
