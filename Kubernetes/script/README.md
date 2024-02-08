# Simple Script

## Copying files into container
Reference: https://loft.sh/blog/kubectl-exec-everything-you-need-to-know/
Reference: https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#cp
Reference: https://stackoverflow.com/questions/12373563/python-try-block-does-not-catch-os-system-exceptions

```py
import os
import subprocess

NAMESPACE = "airflow"
POD_NAME = "airflow-worker-0"
CONTAINER = "worker"

print("Enter the list of files to be copied:")
paths = []

while True:
    path = input()
    if path == "":
        break
    else:
        paths.append(path)

for f in paths:
    rancher_path = f.replace("/var/nas/mnt", "")
    print(f"Copying {f} --> {rancher_path}")

    try:
        subprocess.run(f"kubectl cp {f} {NAMESPACE}/{POD_NAME}:{rancher_path} -c {CONTAINER}".split(), check=True)
    except subprocess.CalledProcessError:
        try:
            print("Retrying with creating folder in rancher")
            folder_path = os.path.dirname(rancher_path)
            print(f"Creating folder {folder_path}")
            subprocess.run(f"kubectl exec --namespace={NAMESPACE} --container={CONTAINER} {POD_NAME} -- mkdir -p {folder_path}".split(), check=True)
            subprocess.run(f"kubectl cp {f} {NAMESPACE}/{POD_NAME}:{rancher_path} -c {CONTAINER}".split(), check=True)
        except subprocess.CalledProcessError:
            print(f"Cannot create folder: {folder_path}")
            exit()

print("STATUS: DONE")
```

## Copying files from container into local
```bash
kubectl cp <namespace>/<pod-name>:/path/to/file/in/container /path/to/local/machine
```
```py
import subprocess

NAMESPACE = "<namespace>"
POD_NAME = "<pod-name>"
CONTAINER = "<container>"
FILE_PATH_IN_CONTAINER = "/path/to/file/in/container"
LOCAL_PATH = input("/path/to/local/machine")

def copy_file_from_container():
    try:
        print(f"Copying {FILE_PATH_IN_CONTAINER} --> {LOCAL_PATH}")
        subprocess.run(f"kubectl cp {NAMESPACE}/{POD_NAME}:{FILE_PATH_IN_CONTAINER} {LOCAL_PATH} -c {CONTAINER}".split(), check=True)
    except subprocess.CalledProcessError:
        print(f"Failed to copy: {FILE_PATH_IN_CONTAINER}")

    print("STATUS: DONE")

if __name__ == "__main__":
    copy_file_from_container()

```