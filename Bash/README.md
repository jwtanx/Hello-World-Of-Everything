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

### Autostart a service
https://unix.stackexchange.com/a/504354
```
[Unit]
Description=My service
[Service]
ExecStart=/path/to/my/script.sh
ExecStop=/usr/bin/killall script.sh

# Useful during debugging; remove it once the service is working
StandardOutput=console

[Install]
WantedBy=multi-user.target
Save it under /etc/systemd/system/myscript.service or any other name,

Then run:

sudo systemctl start myscript
You can check the service with sudo systemctl status myscript and stop with sudo systemctl stop myscript. To make it starts after boot run systemctl enable myscript as root.

sudo systemctl disable testing.service
```

### If Else
#### Operator
| Operator | Description                                                                        | Example                            |
| -------- | ---------------------------------------------------------------------------------- | ---------------------------------- |
| `-e`     | Checks if the file exists.                                                         | `if [ -e "$file" ]; then`          |
| `-f`     | Checks if the file is a regular file (not a directory or device file).             | `if [ -f "$file" ]; then`          |
| `-s`     | Checks if the file is not empty.                                                   | `if [ -s "$file" ]; then`          |
| `-r`     | Checks if the file is readable.                                                    | `if [ -r "$file" ]; then`          |
| `-w`     | Checks if the file is writable.                                                    | `if [ -w "$file" ]; then`          |
| `-x`     | Checks if the file is executable.                                                  | `if [ -x "$file" ]; then`          |
| `-d`     | Checks if the file is a directory.                                                 | `if [ -d "$directory" ]; then`     |
| `-z`     | Checks if the length of the string is zero (i.e., if the string is empty).         | `if [ -z "$string" ]; then`        |
| `-n`     | Checks if the length of the string is non-zero (i.e., if the string is not empty). | `if [ -n "$string" ]; then`        |
| `-gt`    | Checks if one number is greater than another.                                      | `if [ "$num1" -gt "$num2" ]; then` |
| `-lt`    | Checks if one number is less than another.                                         | `if [ "$num1" -lt "$num2" ]; then` |
| `-eq`    | Checks if two numbers are equal.                                                   | `if [ "$num1" -eq "$num2" ]; then` |
| `-ne`    | Checks if two numbers are not equal.                                               | `if [ "$num1" -ne "$num2" ]; then` |
| `-ge`    | Checks if first number is greater than or equals to the second number              | `if [ "$num1" -ge "$num2" ]; then` |

#### Curly Bracket
In the shell script line if ! [[ $is_fe_start ]], the ${} is not used because it's not necessary in this context.
In Bash, you can use $variable or ${variable} to reference the value of a variable. The ${} form is needed when you want to append something directly to the variable's value without a separating space. For example, if you have a variable var="world" and you want to print "helloworld", you would need to use ${var} like this: echo "hello${var}".
In your case, $is_fe_start is alone and not being directly appended with any string, so you can use $is_fe_start instead of ${is_fe_start}.
The [[ $is_fe_start ]] is a conditional expression that checks if the variable is_fe_start is set and is not empty. The ! operator negates the condition. So, if ! [[ $is_fe_start ]] checks if the variable is_fe_start is not set or is empty.

#### Double Parenthesis
In shell scripting, ${} and $(()) are used for different purposes:
${}: This is used for variable substitution. It allows you to get the value of a variable. For example, if you have a variable be_join_status, you can get its value using ${be_join_status}.
$(()): This is used for arithmetic operations. It allows you to perform calculations. For example, $(($i % 20)) is calculating the remainder of the variable $i divided by 20.
In the script you provided, ${be_join_status} is used to get the value of the variable be_join_status, and $(($i % 20)) is used to calculate the remainder of $i divided by 20.

#### Square Brackets, Double Square Brackets
In shell scripting, both single ([ ... ]) and double ([[ ... ]]) square brackets are used for conditional expressions. However, there are some differences between them:
[ ... ]: This is the traditional form for shell scripting. It is POSIX compliant, meaning it will work in any POSIX-compliant shell, like bash, ksh, and sh. However, it has some limitations and quirks, especially when dealing with strings and variables that could be empty or contain spaces.
[[ ... ]]: This is a more modern, bash-specific version. It has several advantages over the traditional form:
Word splitting and filename expansion are not performed on the words between [[ and ]].
It allows for regular expression matching with =~.
It allows for more operators, like string comparison with < and >.
It treats variables in quotes as strings, even if they are empty or undefined.
In general, if you're writing a script specifically for a bash environment, it's often safer and more powerful to use [[ ... ]]. If you're writing a script that needs to be portable across different types of shells, then you should use [ ... ].

#### Summary
| Syntax                       | Description                                                                                                                                                               | Example                                               |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| `$variable` or `${variable}` | Used to reference the value of a variable in Bash. `${variable}` is needed when you want to append something directly to the variable's value without a separating space. | `var="world"`<br>`echo "hello${var}"`                 |
| `! [[ $variable ]]`          | A conditional expression that checks if the variable is not set or is empty.                                                                                              | `if ! [[ $is_fe_start ]]`                             |
| `${}`                        | Used for variable substitution in shell scripting. It allows you to get the value of a variable.                                                                          | `be_join_status="joined"`<br>`echo ${be_join_status}` |
| `$(( ))`                     | Used for arithmetic operations in shell scripting. It allows you to perform calculations.                                                                                 | `i=21`<br>`echo $(($i % 20))`                         |
| `[ ... ]`                    | Traditional form for conditional expressions in shell scripting. It is POSIX compliant.                                                                                   | `if [ $var -gt 10 ]`                                  |
| `[[ ... ]]`                  | A more modern, bash-specific version for conditional expressions. It has several advantages over the traditional form.                                                    | `if [[ $var > 10 ]]`                                  |

### Try and Except
```bash
first_command || second_command_to_run_if_first_command_failed

# Example
lw || ls # lw is not a command so it fail therefore it run ls
ls || lw # lw will not be run
```