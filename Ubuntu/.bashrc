REMINDER="\n`date`\n\n==================\nGOOD DAY J.W. TAN!\n==================\n\nWhen in doubt, hard code!\n"
# 應 無 所 住 , 而 生 其 心

# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples
# ln -s /home/junwei/Desktop/company/data_platform/.ivy2 /tmp 2>/dev/null
cp -r /home/junwei/Desktop/company/data_platform/.ivy2 /tmp

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
# export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# Temporary
alias tbuild="cd ~/Desktop/company && ./bazelisk-linux run //data_platform/data_services/airflow:test_image_publish --verbose_failures && docker pull harbor.company.com/cnx/data_platform/dp-airflow:latest && docker run -d harbor.company.com/cnx/data_platform/dp-airflow:latest sh -c 'sleep infinity'"
alias bbase="cd ~/Desktop/company/data_platform && docker build -f data_services/airflow_build_dev_new.dockerfile -t harbor.company.com/cnx/data_platform/dp-airflow:testing_new --progress=plain --no-cache ."
alias btoml="cp ~/Desktop/company/data_platform/pyproject.toml ~/Desktop/company/ && cd ~/Desktop/company && rm -rf data_platform/data_services/opt && p -m build -w -o data_platform/data_services/opt . && rm ~/Desktop/company/pyproject.toml"

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias p='python3'
alias clip='xclip -sel clip'
alias gp="git push origin HEAD:refs/for/master"
alias gb="git branch"
alias yf='yapf -i "--style={based_on_style: google, column_limit: 80, indent_width: 2}" -r'
alias yf2='yapf -i "--style={based_on_style: google, column_limit: 80, indent_width: 2, spaces_before_comment: 2, split_before_logical_operator: true}" -r'
alias yfq='~/Desktop/company/data_platform/.venv/3.10/yapf-3.10/bin/python -m yapf -i "--style={based_on_style: google, column_limit: 80, indent_width: 2}" --fixers quotes --force-quote-type double -r'
alias format_bazel='~/Desktop/company/bazelisk-linux run //:buildifier_format'
alias shit='shutdown -P 0'
alias findnewjob='shutdown -P 0'
alias de='deactivate'
alias asdf='sudo su'
alias size='du -sh */ | sort -hr'
alias filesize='du -sh | sort -h'
alias cd..='cd ..'
alias chmod777dir='find . -type d -exec chmod 777 {} \;'
alias cmd='gnome-terminal'
alias cdc='cd /home/junwei/Desktop/company/data_platform'
alias cdcd='cd /home/junwei/Desktop/company/data_platform/data_services'
alias mlserver='ssh junwei@192.168.xxx.xxx'
alias base='base64 -w 0'
alias ddownr='docker compose down ; git restore docker-compose.yaml'
alias ddown='docker compose down'
alias dup='docker compose up -d'
alias ddup='cd /home/junwei/Desktop/company/data_platform/data_services && cat "temp/ref/docker-compose - full.yaml" > docker-compose.yaml && docker compose up -d'
alias dp='docker ps'
alias dpa='docker ps -a'
alias dclear='docker builder prune'
alias dsize='docker system df'
alias dback='docker images --no-trunc --format "{\"name\": \"{{.Repository}}\", \"tag\": \"{{.Tag}}\", \"size\": \"{{.Size}}\", \"digest\": \"{{.ID}}\"}" | jq -s "." > docker_images.json'
alias drmimage='docker rmi $(docker images -f "dangling=true" -q)'
alias linkfolder='find ~/Desktop/company/data_platform/data_pipelines/ -type f -name "*.py" -exec ln -s -t ~/airflow/dags/ {} +'
alias actmix='. /home/junwei/Desktop/company/data_platform/.venv/3.10/mix-3.10/bin/activate'
alias actcog='. /home/junwei/Desktop/company/data_platform/.venv/3.10/cogdata-env/bin/activate'
alias pid='ps aux'
alias di='docker images'
alias adl='rm -rf ~/airflow/dags/* ; find ~/Desktop/company/data_platform/data_pipelines/ -type f -name "*.py" -exec ln -s -t ~/airflow/dags/ {} + &> /dev/null; airflow dags list'
alias hfcache="cd ~/.cache/huggingface/hub"
alias robo="DISABLE_WAYLAND=1 robo3t-snap"
# alias robo="WAYLAND_DISPLAY=wayland-1 ; robo3t-snap"
alias k='kubectl'
alias mk='minikube'
alias myip="ip addr | grep noprefix | grep -oP 'inet \K\S+' | cut -d'/' -f1"

# Bazel test the current folder
test_bazel() {
    if [ -n "$1" ]; then
        cur_dir=$(realpath $1 | sed 's/home\/junwei\/Desktop\/company//g')
    else
        cur_dir=$(pwd | sed 's/home\/junwei\/Desktop\/company//g')
    fi

    if [ -z "$2" ]; then
        ~/Desktop/company/bazelisk-linux test $cur_dir/... --test_output=all
    else
        ~/Desktop/company/bazelisk-linux test $cur_dir/... --test_output=all --cache_test_results=no
    fi
}

# Docker services: User variables
AIRFLOW_UID=1001
export PATH=$PATH:$(go env GOPATH)/bin
export MLFLOW_SERVER_URI=http://127.0.0.1:5000
export MLFLOW_API_HOST=127.0.0.1
export MLFLOW_TRACKING_URI=http://127.0.0.1:5000
export MLFLOW_TRACKING_USERNAME=xxx
export MLFLOW_TRACKING_PASSWORD=xxx
export IP=$(ip addr | grep noprefix | grep -oP 'inet \K\S+' | cut -d'/' -f1)
export SUPERSET_SECRET_KEY=xxx
export AIRFLOW_UID=1001
export AIRFLOW__CORE__LOAD_EXAMPLES='false'
export KUBECONFIG=~/.kube/test-cloud.yaml

kill_port() {
    kill -9 $(lsof -t -i:$1)
}

pidinfo() {
    lsof -p "$1" | grep cwd
}

dr() {
    if [ -n "$2" ]; then
        docker run -d --name "$2" "$1" busybox sh -c "sleep infinity"
    else
        docker run -d "$1" busybox sh -c "sleep infinity"
    fi
}

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

# Enable ctrl + backspace to remove a word in terminal
stty werase \^H


# VS Code Python Venv Activation
# This file must be used with "source bin/activate" *from bash*
# You cannot run it directly
# _OLD_VIRTUAL_PS1="${PS1:-}"
# _OLD_VIRTUAL_PATH="$PATH"
# if [ -n "${PYTHONHOME:-}" ] ; then
#     _OLD_VIRTUAL_PYTHONHOME="${PYTHONHOME:-}"
# fi

# deactivate () {
#     # reset old environment variables
#     if [ -n "${_OLD_VIRTUAL_PATH:-}" ] ; then
#         PATH="${_OLD_VIRTUAL_PATH:-}"
#         export PATH
#         unset _OLD_VIRTUAL_PATH
#     fi
#     if [ -n "${_OLD_VIRTUAL_PYTHONHOME:-}" ] ; then
#         PYTHONHOME="${_OLD_VIRTUAL_PYTHONHOME:-}"
#         export PYTHONHOME
#         unset _OLD_VIRTUAL_PYTHONHOME
#     fi

#     # This should detect bash and zsh, which have a hash command that must
#     # be called to get it to forget past commands.  Without forgetting
#     # past commands the $PATH changes we made may not be respected
#     if [ -n "${BASH:-}" -o -n "${ZSH_VERSION:-}" ] ; then
#         hash -r 2> /dev/null
#     fi

#     if [ -n "${_OLD_VIRTUAL_PS1:-}" ] ; then
#         PS1="${_OLD_VIRTUAL_PS1:-}"
#         export PS1
#         unset _OLD_VIRTUAL_PS1
#     fi

#     unset VIRTUAL_ENV
#     unset VIRTUAL_ENV_PROMPT
#     if [ ! "${1:-}" = "nondestructive" ] ; then
#     # Self destruct!
#         unset -f deactivate
#     fi
# }

bash ~/shrunner.sh
echo -e $REMINDER
