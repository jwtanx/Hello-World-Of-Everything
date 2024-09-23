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

## Double pipe to run another command
```bash
# If the first command fails, run the second command
command1 || command2
```

## Suppressing regular output, error output or both
```bash
# Suppressing regular output
command > /dev/null

# Suppressing error output
command 2> /dev/null

# Suppressing both
command &> /dev/null
```


## Adding startup sound
https://askubuntu.com/questions/1450618/how-to-enable-startup-sound-in-ubuntu-22-04-1-lts
1. Search Startup Applications
2. Add a new entry
3. Name: Startup Sound
4. Windows XP file can be found [here](../Windows%20CMD/src/windows-xp-startup.ogg)
5. Possible commands:
```bash
# For this to work, you have to copy the ogg sound file and place in /usr/share/sounds/Yaru/stereo
/usr/bin/canberra-gtk-play --id="desktop-login" --description="GNOME login"
/usr/bin/canberra-gtk-play --id="windows-xp-startup" --description="GNOME login"

paplay /usr/share/sounds/ubuntu/stereo/desktop-login.ogg
paplay /usr/share/sounds/Yaru/stereo/desktop-login.ogg
```

## Adding logoff / shutdown sound
https://ubuntuforums.org/showthread.php?t=2485860
1. Change directory to /usr/lib/systemd/system-shutdown
2. Add the following code to a script named "windows-shutdown.sh"
3. Script content
```bash
#!/bin/sh
mpv /usr/share/sounds/Yaru/stereo/windows-xp-shutdown.ogg
```
> To add a new sound, you can use the following command
```sh
sudo cp /path/to/windows-xp-shutdown.ogg /usr/share/sounds/Yaru/stereo
```
You may download here [windows-xp-shutdown.ogg](../Windows%20CMD/src/windows-xp-shutdown.ogg)

4. Make it executable
```bash
sudo chmod +x windows-shutdown.sh
```

## Shortcut to copy password to clipboard
1. Create a new profile in the terminal
2. Set the profile to have small windows size
3. Go to shortcut and add the following command with your special combination of key press
```
gnome-terminal --window-with-profile=Background -x sh -c 'echo -n YOUR_PASSWORD | xclip -sel clip ; sleep 0.1'
```

## Adding content into a file without opening it
```bash
cat <<EOF>> /path/to/file
This is a long long passage
that I can write with my environment variable: ${USER}
EOF
```

## Overwrite the content of a file
```bash
cat <<EOF> /path/to/file
This is a long long passage
EOF
```

## Getting only the filename, removing the path name
https://stackoverflow.com/questions/9011233/for-files-in-directory-only-echo-filename-no-path
```bash
basename /path/to/file
echo /path/to/file | rev | cut -d'/' -f1 | rev
echo /path/to/file | awk -F/ '{print $NF}'
echo /path/to/file | sed 's/.*\///'
```
OR
```bash
for file in /home/user/*; do
  echo "${file##*/}"
done
```

## Connect to a port, can't use ping
```bash
nc -zv google.com 443
telnet google.com 443
```

## GREP - Global Regular Expression Print
```bash
# Find all the files that contain the word "hello"
grep -r "hello" /path/to/directory

# Find the pattern in any command
history | grep "pattern"
```

## EGREP - Extended GREP
```bash
# Find all the files that contain the word "hello" or "world"
egrep -r "hello|world" /path/to/directory

# Multiple patterns
ls -la | egrep "hello|world|goodbye"
```
