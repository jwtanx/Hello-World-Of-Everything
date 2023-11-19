# Bash

## Remove word using CTRL + Backspace in gnome terminal
Reference: https://askubuntu.com/questions/701824/getting-ctrl-backspace-to-delete-words-in-gnome-terminal-and-vim-insert-mo
In `~/.bashrc`, add this in
```
stty werase \^H
```
For adding this function in root terminal, add the line into /root/.bashrc

## Curls
### Downloading Google Drive files using curl
Reference: https://stackoverflow.com/a/73893665
FILE_ID = "1eHvVuOZdXYtuavrW-N32EcHJXjLsa1xs"
curl -L 'https://drive.google.com/uc?export=download&id=FILE_ID&confirm=t' > FILENAME.EXT

## Hostname
```bash
command = "hostname -i"
docker_ip = subprocess.check_output(command, shell=True, text=True).strip()
Use regex to replace the last octet to 1
```

## SCP
### Send file to a remote computer:

```bash
scp /file/to/send username@remote:/where/to/put
```

### Receive file from a remote computer:
```bash
scp username@remote:/file/to/send /where/to/put
```