# Terraform
- Open-source infrastructure as code software tool created by HashiCorp.
- Enables users to define and provision a datacenter infrastructure using a high-level configuration language known as Hashicorp Configuration Language, or optionally JSON.

## Quick Example
```hcl
provider "aws" {
  region = "us-west-2"
}

resource "google compute_instance" "mom" {
  machine_type = "e2-medium"
  zone = "us-central1-a"
}

resource "aws_instance" "dad" {
  instance_type = "t3.large"
  availability_zone = "us-west-2a"
}
```

## Features
- Human readable blueprint that can execute and automate everything you do in cloud
- Save time clicking the buttons in the cloud console
- Version control your infrastructure

## Quick Start
1. Install Terraform
https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli
```sh
# Ensure gnupg, software-properties-common, and curl are installed
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common

# Install the HashiCorp GPG key.
wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null

# Verify the key's fingerprint.
gpg --no-default-keyring --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg --fingerprint

# Add the official HashiCorp repository to your system
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list

# Update and install
sudo apt update
sudo apt-get install terraform
```

2. Verify the installation
```sh
terraform -help
```

3. Enable tab completion
```sh
# Make sure you have ~/.bashrc, if not create it
touch ~/.bashrc

# Run the below command
terraform -install-autocomplete
# complete -C /usr/bin/terraform terraform
# ^ This line will be added into ~/.bashrc
```

4. Trial with project
```sh
cd project

# Initialize the project
terraform init

# Save the plan into a binary file
terraform plan -out plan.out

# Show the plan
terraform show plan.out

# Apply the plan
terraform apply

# To see the current state
terraform show

# Check your docker containers
docker ps
# CONTAINER ID   IMAGE             COMMAND                  CREATED         STATUS                      PORTS                  NAMES
# 671ec80d8207   92b11f67642b      "/docker-entrypoint.…"   6 seconds ago   Up 6 seconds                0.0.0.0:8000->80/tcp   tutorial

# Destroy the infrastructure
terraform destroy
```
5. When we have a new version of the code
```sh
# Update the project
terraform apply
```

6. Restart
```sh
# Restart the project
terraform apply
```

## Declarative vs Imperative
### Declarative Approach
- Instead of telling Terraform what steps to be executed, you define the end state of what you desire, let Terraform figures out how to make it happen
- Terraform will create a plan to make the current state match the desired state

### Imperative Approach
- You tell Terraform what to do

### Example
| Imperative                                                                   | Declarative (Give them your new desired state)                        |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Please remove 2 servers                                                      | I want 7 servers                                                      |
| Please add firewall config                                                   | I want this firewall config                                           |
| Please add permissions to AWS user                                           | I want this user to have these permissions                            |
| Need to figure out the delta of the changes applied by multiple instructions | Readjust old config file and re-execute                               |
|                                                                              | Congifuration file stays clean and small                              |
|                                                                              | Always know the current setup, because that is always the end results |

## Terraform Commands

| Command                  | Description                                                             |
| ------------------------ | ----------------------------------------------------------------------- |
| `terraform init`         | Initialize a working directory containing Terraform configuration files |
| `terraform plan`         | Generate and show an execution plan                                     |
| `terraform apply`        | Builds or changes infrastructure                                        |
| `terraform show`         | Provide human-readable output from a state or plan file                 |
| `terraform destroy`      | Destroy the Terraform-managed infrastructure                            |
| `terraform fmt`          | Rewrites config files to canonical format                               |
| `terraform refresh`      | Update the state to match remote systems                                |
| `terraform import`       | Associate existing infrastructure with a Terraform resource             |
| `terraform validate`     | Validates the configuration files in a directory                        |
| `terraform taint`        | Manually mark a resource for recreation                                 |
| `terraform untaint`      | Manually unmark a resource as tainted                                   |
| `terraform output`       | Read an output from a state file                                        |
| `terraform state`        | Advanced state management                                               |
| `terraform workspace`    | Workspace management                                                    |
| `terraform console`      | Interactive console for evaluating expressions                          |
| `terraform force-unlock` | Release a stuck lock on the current workspace                           |
| `terraform login`        | Obtain and save credentials for a remote host                           |
| `terraform logout`       | Remove locally-stored credentials for a remote host                     |
| `terraform version`      | Show the current Terraform version                                      |
| `terraform providers`    | Show the providers required for this configuration                      |

