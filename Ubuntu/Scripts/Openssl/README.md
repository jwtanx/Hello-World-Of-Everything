# Openssl

## Quick Start
openssl pkeyutl -encrypt -pkeyopt rsa_padding_mode:oeap -inkey public.pem -in secret.txt -pubin | openssl base64

## Advanced
openssl base64 -d -in encrypted.txt | openssl pkeyutl -decrypt -inkey private.pem -pkeyout rsa_padding_mode:oeap -out decrypted.txt
