# Vault Agent Quick Guide
1. Using root to create a [vault.sh](./vault.sh)
```sh
sudo nano ~/vault.sh
# Copy and paste the code from vault.sh
```
2. Store [vault.sh](./vault.sh) in HOME directory where the .zshrc or .bashrc is located.
3. Change the permission to read and write only for the owner 
```sh
sudo chmod 600 ~/vault.sh
```
4. Paste the code of [.zshrc](./.zshrc) into your own .zshrc or .bashrc
5. Run the below command
```sh
# To get AWS credential
get aws
```
6. Enter password and your credential is copied to your clipboard