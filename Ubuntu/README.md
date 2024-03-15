# Ubuntu

## Viewing output in real time for command
https://stackoverflow.com/questions/8223811/a-top-like-utility-for-monitoring-cuda-activity-on-a-gpu
watch -n 1 nvidia-smi

## Finding a file from a directory
```bash
# Finding any file that has the extension .csv with suffix _done
find . -type f -name *_done.csv
```

## Remove the list of files with suffix
```bash
rm $(find . -type f -name *.cache)
```

## Getting the full path of the current files that ends with .csv
```bash
realpath *.csv
```

## Stop process: Device or resource busy
https://unix.stackexchange.com/questions/11238/how-to-get-over-device-or-resource-busy
```bash
lsof +D /path
lsof +D ./ | awk '{print $2}' | tail -n +2 | xargs -r kill -9
```

## Linking symbolic link for the folder
ln -s /original/data/path /path/to/add/link

## Base64: Encode and Decoding
```bash
# Encoding
echo -n "password" | base64
# cGFzc3dvcmQ=

# Decoding
echo -n "cGFzc3dvcmQ=" | base64 -d
# password
```
-n: no new line