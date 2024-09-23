# SSM (Parameter Store)
## Getting the value of a parameter
```bash
# Non decrypted
aws ssm get-parameter --name demo-param --query Parameter.Value --output text

# Decrypt
aws ssm get-parameter --name demo-param --query Parameter.Value --with-decryption --output text
```

## Getting the value based on the version
```bash
# For version 1
aws ssm get-parameters --names demo-param:1 --with-decryption

# For version 2
aws ssm get-parameters --names demo-param:2 --with-decryption
```