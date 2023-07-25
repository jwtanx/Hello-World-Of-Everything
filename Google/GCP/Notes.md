# Google Cloud Platform CLI Cheat Sheet

[Good Reference](https://jayendrapatil.com/google-cloud-gcloud-cheat-sheet)

## Google Cloud - `gcloud`
[Complete Reference](https://cloud.google.com/sdk/docs/cheatsheet)

### Config
| Command Example                           | Description        | Example          |
| ----------------------------------------- | ------------------ | ---------------- |
| gcloud config set compute/region <region> | Set default region | region: us-west1 |
| gcloud config set compute/zone <zone>     | Set default zone   | zone: us-west1-b |



## container clusters
- Provision a Kubernetes cluster using Kubernetes Engine
gcloud container clusters create jenkins-cd \
--num-nodes 2 \
--scopes "https://www.googleapis.com/auth/projecthosting,cloud-platform"


## Google Cloud Storage - `gsutil`

PURPOSE	COMMAND
List all buckets and files	gsutil ls, gsutil ls -lh gs://<bucket-name>
Create bucket	gsutil mb gs://<bucket-name>
Download file	gsutil cp gs://<bucket-name>/<dir-path>/app.txt
Upload file	gsutil cp <filename> gs://<bucket-name>/<directory>/
Delete file	gsutil rm gs://<bucket-name>/<filepath>
Move file	gsutil mv <src-filepath> gs://<bucket-name>/<directory>/<dest-filepath>
Copy folder	gsutil cp -r ./conf gs://<bucket-name>/
Show disk usage	gsutil du -h gs://<bucket-name/<directory>
Make all files readable	gsutil -m acl set -R -a public-read gs://<bucket-name>/
Create signed url with duration	gsutil signurl -d 1m
gsutil mb -c regional -l us-east1 gs://$BUCKET

Enable versioning on the bucket so that you have a history of your manifests:
gsutil versioning set on gs://<bucket-name>


---

gsutil is Google Storage CLI tool. Equivalent to aws s3 but for the Google Cloud Platform, it allows you to access Google Cloud Storage from the command line. Beyond moving files and managing buckets, gsutil is a powerful file management (rsync) and file publication tool (signed urls).

Please find below a shortlist of the most important and frequent commands and their relative syntax.

This is a work in progress that will be updated within the next few days.

Gsutil cheatsheet
gsutil is Google Cloud storage CLI. More info on

Definitions
GCP: Google Cloud Platform
Install
To get started with gsutil you need python (at least 2.7) and to install the Google Cloud SDK. See https://cloud.google.com/sdk/docs/ to download the right package for your environment.

General Commands
gsutil ls: lists all your buckets
gsutil help <topic>: help on the topic
Buckets
gsutil mb gs://<bucket_name>: creates the gs://bucket_name1.

gsutil rb gs://<bucket_name>: deletes the bucket.

Files
gsutil cp <filename> gs://<bucket_name>/: copies the local filename into the bucket ****.

gsutil cp <filename> gs://<bucket_name>/directory/: copies the local filename into the directory ****2.

gsutil mv <src_filename> gs://<bucket_name>/directory/<tgt_filename>: moves the local src_filename to the directory and renames it as tgt_filename

gsutil rm gs://<bucket_name>/file_or_dir: deletes the file_or_dir object.

Folder
gsutil cp <filename> gs://<bucket_name>/: copies the local filename into the bucket ****.
Footnotes
1: The bucket name has to be unique across GCP.
2: Note the trailing ‘/’ slash after < directory > to tell gsutil that the target is a directory and not a file

---
gsutil cheatsheet
The following is a list of the most-used commands that we can issue via gsutil:

Creating a bucket named packt-gcp:
gsutil mb gs://packt-gcp
Uploading a file to the bucket:

gsutil cp gs://packt-gcp/
Creating a subfolder in the bucket:
gsutil cp your-file gs://packt-gcp/
Listing the folder:
gsutil ls gs://packt-gcp/
Getting help on gsutil commands:
gsutil help
How much storage are we using (the -h makes it readable):
gsutil du -h gs://packt-gcp/
Copying a whole folder to a bucket:
gsutil cp -r gs://packt-gcp/
For instance, I have a local ./img directory with some images. I can copy the whole directory and create the bucket subdirectory at the same time with the following command:

gsutil cp -r ./img ...


## Big Query - `bq`



Google Cloud Config
PURPOSE	COMMAND
List projects	gcloud config list, gcloud config list project
List projects	gcloud config list, gcloud config list project
Show project info	gcloud compute project-info describe
Switch project	gcloud config set project <project-id>
Set the active account	gcloud config set account <ACCOUNT>
Set default region	gcloud config set compute/region us-west
Set default zone	gcloud config set compute/zone us-west1-b
List configurations	gcloud config configurations list
Activate configuration	gcloud config configurations activate

Google Cloud IAM
PURPOSE	COMMAND
get project roles	gcloud projects get-iam-policy
copy roles across org and projects	gcloud iam roles copy
get project roles	gcloud projects get-iam-policy
copy roles across org and projects	gcloud iam roles copy

Google Cloud Auth
PURPOSE	COMMAND
Display a list of credentialed accounts	gcloud auth list
Authenticate client using service account	gcloud auth activate-service-account --key-file <key-file>
Auth to GCP Container Registry	gcloud auth configure-docker
Print token for active account	gcloud auth print-access-token, gcloud auth print-refresh-token
Revoke previous generated credential	gcloud auth <application-default> revoke

Google Cloud Storage
PURPOSE	COMMAND
List all buckets and files	gsutil ls, gsutil ls -lh gs://<bucket-name>
Create bucket	gsutil mb gs://<bucket-name>
Download file	gsutil cp gs://<bucket-name>/<dir-path>/app.txt
Copy file in multithread gsutil -m cp -r gs://<bucket-name>/<dir-path> .
Upload file	gsutil cp <filename> gs://<bucket-name>/<directory>/
Delete file	gsutil rm gs://<bucket-name>/<filepath>
Move file	gsutil mv <src-filepath> gs://<bucket-name>/<directory>/<dest-filepath>
Copy folder	gsutil cp -r ./conf gs://<bucket-name>/
Show disk usage	gsutil du -h gs://<bucket-name/<directory>
Make all files readable	gsutil -m acl set -R -a public-read gs://<bucket-name>/
Create signed url with duration	gsutil signurl -d 1m

Google Kubernetes Engine
PURPOSE	COMMAND
- create cluster
gcloud container clusters create cluster-name --num-nodes 1
- List all container clusters
gcloud container clusters list
- Set kubectl context
gcloud container clusters get-credentials <cluster-name>
- Set default cluster
gcloud config set container/cluster cluster-name
- resize existing cluster
gcloud container clusters resize --num-nodes

Google Cloud Compute Engine
PURPOSE	COMMAND
List all instances	gcloud compute instances list , gcloud compute instance-templates list
Show instance info	gcloud compute instances describe "<instance-name>" --project "<project-name>" --zone "us-west2-a"
Stop an instance	gcloud compute instances stop instance-name
Start an instance	gcloud compute instances start instance-name
Create an instance	gcloud compute instances create vm1 --image image-1 --tags test --zone "<zone>" --machine-type f1-micro
Create premptible instance	gcloud compute instances create "preempt" --preemptible
SSH to instance	gcloud compute ssh --project "<project-name>" --zone "<zone-name>" "<instance-name>"

gcloud compute instances create ad-dc1 --machine-type n1-standard-2 \
    --boot-disk-type pd-ssd \
    --boot-disk-size 50GB \
    --image-family windows-2016 --image-project windows-cloud \
    --network ${vpc_name} \
    --zone ${zone_1} --subnet private-ad-zone-1 \
    --private-network-ip=10.1.0.100

Images list	gcloud compute images list

Virtual Private Network
PURPOSE	COMMAND
List all networks	gcloud compute networks list
Detail of one network	gcloud compute networks describe <network-name> --format json
Create network	gcloud compute networks create <network-name>
gcloud compute networks create ${vpc_name}  \
    --description "VPC network to deploy Active Directory" \
    --subnet-mode custom

Create subnet	gcloud compute networks subnets create subnet1 --network subnet-1 --range 10.0.0.0/24
gcloud compute networks subnets create private-ad-zone-1 \
    --network ${vpc_name} \
    --range 10.1.0.0/24 \
    --region ${region1}

List all firewall rules	gcloud compute firewall-rules list
List all forwarding rules	gcloud compute forwarding-rules list
Describe one firewall rule	gcloud compute firewall-rules describe <rule-name>
Create firewall rule	gcloud compute firewall-rules create my-rule --network default --allow tcp:22
Update firewall rule	gcloud compute firewall-rules update default --network default --allow tcp:80

Components
PURPOSE	COMMAND
List down the components	gcloud components list
Update the components	gcloud components update
Install the components	gcloud components install <component-name>
Deployment Manager
PURPOSE	COMMAND
Create deployments	gcloud deployment-manager deployments create
Update deployments	gcloud deployment-manager deployments update


https://medium.com/@raigonjolly/cheat-sheets-gcloud-bq-gsutil-kubectl-for-google-cloud-associate-certificate-4093b8977a01

Cloud Repos
PURPOSE COMMAND
Create google repo in the source repos  gcloud source repos create sample-app


gcloud compute reset-windows-password ad-dc1 --zone ${zone_1} --quiet --user=admin

Save to container registry
gcloud builds submit --tag gcr.io/$PROJECT/locust-tasks:latest docker-image/.

Deploy the app to your project
gcloud app deploy sample-webapp/app.yaml