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

## SSM and KMS
```py
import boto3
import base64
kms = boto3.client('kms')
ssm = boto3.client('ssm')
from botocore.exceptions import ClientError

cipher_text = ssm.get_parameter(
    Name='secret-parameter',
    WithDecryption=True
)['Parameter']['Value']

key_id = "abcd-1234-efgh-5678"


try:
    kms.decrypt(
        CiphertextBlob=base64.b64decode(cipher_text),
        KeyId=key_id,
        EncryptionAlgorithm='RSAES_OAEP_SHA_1'
    )['Plaintext'].decode('utf-8')
except ClientError as e:
    print(f"Error decrypting parameter: {e.response['Error']['Message']}")

```