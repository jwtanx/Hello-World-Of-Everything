# Google Cloud Platform CLI

## Reference
- https://jayendrapatil.com/google-cloud-gcloud-cheat-sheet
- https://cloud.google.com/sdk/docs/cheatsheet

## Installation


## Google Cloud - `gcloud`
Getting the list of the configuration
```cat ~/.config/gcloud/configurations/config_default```

### Config
| Command Example                             | Description            |
| ------------------------------------------- | ---------------------- |
| `gcloud config set compute/region <region>` | Set default region     |
| `gcloud config set compute/zone <zone>`     | Set default zone       |
| `gcloud config list`                        | List projects          |
| `gcloud config list project`                | List projects          |
| `gcloud compute project-info describe`      | Show project info      |
| `gcloud config set project <project_id>`    | Switch project         |
| `gcloud config set account <account>`       | Set the active account |
| `gcloud config configurations list`         | List configurations    |
| `gcloud config configurations activate`     | Activate configuration |

### Compute
| Command Example                                                                                         | Description                |
| ------------------------------------------------------------------------------------------------------- | -------------------------- |
| `gcloud compute instances list`, `gcloud compute instance-templates list`                               | List all instances         |
| `gcloud compute instances describe "<instance_name>" --project "<project_name>" --zone <zone>`          | Show instance info         |
| `gcloud compute instances stop instance-name`                                                           | Stop an instance           |
| `gcloud compute instances start instance-name`                                                          | Start an instance          |
| `gcloud compute instances create lab-1 --zone us-east4-c --machine-type=e2-standard-2`                  | Basic instance creation    |
| `gcloud compute instances create vm1 --image image-1 --tags test --zone <zone> --machine-type f1-micro` | Create an instance         |
| `gcloud compute instances create "preempt" --preemptible`                                               | Create premptible instance |
| `gcloud compute ssh --project "<project_name>" --zone "<zone>" "<instance_name>"`                       | SSH to instance            |
| `gcloud compute images list`                                                                            | List all images            |


gcloud compute instances create ad-dc1 --machine-type n1-standard-2 \
    --boot-disk-type pd-ssd \
    --boot-disk-size 50GB \
    --image-family windows-2016 --image-project windows-cloud \
    --network ${vpc_name} \
    --zone ${zone_1} --subnet private-ad-zone-1 \
    --private-network-ip=10.1.0.100

gcloud compute zones list

gcloud --version
Start a new gcloud configuration for the second user account. Inside the SSH session run:
gcloud init --no-launch-browser
Choose create a new configuration and put a config name

How to switch back to the first user?
Change back to your first user's configuration (default). Inside the SSH session run:
gcloud config configurations activate default

Check the list of the users
gcloud config configurations list


## container clusters
- Provision a Kubernetes cluster using Kubernetes Engine
gcloud container clusters create jenkins-cd \
--num-nodes 2 \
--scopes "https://www.googleapis.com/auth/projecthosting,cloud-platform"

delete
gcloud container clusters delete private-cluster --zone=$ZONE

update
gcloud container clusters update private-cluster2 \
    --enable-master-authorized-networks \
    --zone=$ZONE \
    --master-authorized-networks [MY_EXTERNAL_RANGE]

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
bq query --location=us --use_legacy_sql=false --use_cache=false \
'select CONCAT(departure_airport, "-", arrival_airport) as route, count(*) as numberflights
 from `bigquery-samples.airline_ontime_data.airline_id_codes` ac,
 `qwiklabs-resources.qlairline_ontime_data.flights` fl
 where ac.code = fl.airline_code
 and regexp_contains(ac.airline ,  r"Alaska")
 group by 1
 order by 2 desc
 LIMIT 10'

## Cloud SQL
gcloud sql connect postgresql-cloudsql --user=postgres --quiet




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
gcloud auth login

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

Creating kubernetes private cluster
gcloud beta container clusters create private-cluster \
    --enable-private-nodes \
    --master-ipv4-cidr 172.16.0.16/28 \
    --enable-ip-alias \
    --create-subnetwork ""



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
gcloud compute networks subnets create my-subnet \
    --network default \
    --range 10.0.4.0/22 \
    --enable-private-ip-google-access \
    --region=$REGION \
    --secondary-range my-svc-range=10.0.32.0/20,my-pod-range=10.4.0.0/14


gcloud compute networks create taw-custom-network --subnet-mode custom
export VPC_NAME=vpc-network-oka3
export SUBNET_A=subnet-a-iclf
export REGION_A=asia-northeast1
export SUBNET_B=subnet-b-zm1l
export REGION_B=europe-west1
gcloud compute networks create $VPC_NAME --project=$DEVSHELL_PROJECT_ID --subnet-mode=custom --mtu=1460 --bgp-routing-mode=regional && gcloud compute networks subnets create $SUBNET_A --project=$DEVSHELL_PROJECT_ID --range=10.10.10.0/24 --stack-type=IPV4_ONLY --network=$VPC_NAME --region=$REGION_A && gcloud compute networks subnets create $SUBNET_B --project=$DEVSHELL_PROJECT_ID --range=10.10.20.0/24 --stack-type=IPV4_ONLY --network=$VPC_NAME --region=$REGION_B

gcloud compute networks subnets create network-a-subnet --network network-a \
    --range 10.0.0.0/16 --region us-west1 

Listing the subnet
gcloud compute networks subnets list \
   --network taw-custom-network
gcloud compute networks subnets list --network default

Describing the subnet
gcloud compute networks subnets describe [SUBNET_NAME] --region=$REGION

List all firewall rules	gcloud compute firewall-rules list
List all forwarding rules	gcloud compute forwarding-rules list
Describe one firewall rule	gcloud compute firewall-rules describe <rule-name>
Create firewall rule	gcloud compute firewall-rules create my-rule --network default --allow tcp:22
Update firewall rule	gcloud compute firewall-rules update default --network default --allow tcp:80
gcloud compute --project=$DEVSHELL_PROJECT_ID firewall-rules create $FIREWALL_RULE_NAME_1 --direction=INGRESS --priority=65535 --network=$VPC_NAME --action=ALLOW --rules=tcp:22 --source-ranges=0.0.0.0/0
gcloud compute --project=$DEVSHELL_PROJECT_ID firewall-rules create $FIREWALL_RULE_NAME_2 --direction=INGRESS --priority=65535 --network=$VPC_NAME --action=ALLOW --rules=tcp:3389 --source-ranges=0.0.0.0/0
gcloud compute --project=$DEVSHELL_PROJECT_ID firewall-rules create $FIREWALL_RULE_NAME_3 --direction=INGRESS --priority=65535 --network=$VPC_NAME --action=ALLOW --rules=icmp --source-ranges=0.0.0.0/0

gcloud compute firewall-rules create nw101-allow-http \
--allow tcp:80 --network taw-custom-network --source-ranges 0.0.0.0/0 \
--target-tags http

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

### List of regions & zones
