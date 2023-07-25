# Kubernetes Cheat Sheet

| Commands                                                                        | Description                                                                  |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| kubectl cluster-info                                                            | Confirm that you can connect to your cluster                                 |
| kubectl get pods                                                                | Check the rediness, status and the age of the pods                           |
| kubectl --namespace default port-forward <path/to/svc> 8080:8080 >> /dev/null & | Port forwarding the service to a port number                                 |
| kubectl get svc                                                                 | Get the list of services (NAME, TYPE, CLUSTER-IP, EXTERNAL-IP, PORT(S), AGE) |

## Other
kubectl exec --namespace default -it svc/myjenkins -c jenkins -- /bin/cat /run/secrets/additional/chart-admin-password && echo
kubectl run -it --rm alpine --image=alpine:3.6 --restart=Never nslookup mycache-memcached.default.svc.cluster.local

To confirm that the locust-master pod is created, run the following command:
kubectl get pods -l app=locust-master

kubectl scale deployment/locust-worker --replicas=20