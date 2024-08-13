REMINDER="\n`date`\n\n==================\nGOOD DAY J.W. TAN!\n==================\n\nWhen in doubt, hard code!\n應 無 所 住 , 而 生 其 心\n"

# Prefix
PS1="%F{208}%n%F{037}@windows-xp %1 %F{255}λ %F{255}"

# Bindkey
# bindkey '^H' backward-kill-word
# bindkey '^[[3;5~' backward-kill-word

# Export
export FUNCTIONS_CORE_TOOLS_TELEMETRY_OPTOUT=1
export NVM_DIR="$HOME/.nvm"
  [ -s "/opt/homebrew/opt/nvm/nvm.sh" ] && \. "/opt/homebrew/opt/nvm/nvm.sh"  # This loads nvm
  [ -s "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm" ] && \. "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm"  # This loads nvm bash_completion
export LOCAL_VERSION='v1.1.7'
export PATH=$HOME/bin:$PATH

# Alias
alias config='code ~/.zshrc'
alias ll='ls -la'
alias gb="git branch"
alias gc="git commit"
alias gp='git push origin $(git branch --show-current)'
alias gpf='git push origin $(git branch --show-current) --force-with-lease'
alias tfmt='cd ~/Desktop/repos/infra ; git diff --name-only --diff-filter=AM | grep .tf$ | xargs -I {} terraform fmt {}; cd - > /dev/null'
alias cdc='cd ~/Desktop/repos'
alias cd..='cd ..'
alias pip='/opt/homebrew/bin/pip3'
alias pb='pbcopy'
alias tf='~/bin/terraform'
alias ac='. env/bin/activate'
alias de='deactivate'
alias pip='pip3'
alias p='python'
alias p3='python3'
alias gerp='grep'
alias fast='echo -n "document.getElementsByClassName(\"video-stream html5-main-video\")[0].playbackRate = 3" | pb'

## My repo
alias note='code ~/Desktop/my-repo/Hello-World-Of-Everything'

# Unlink /usr/local/bin/code after restarting
alias uncode='sudo rm /usr/local/bin/code'

## My app
alias ocr='cd ~/Desktop/my-repo/Screenshot2Text ; env/bin/python3 ocr.py'

## Docker
alias cs='colima start --memory 8'
alias dpa='docker ps -a'
alias di='docker images'
alias dclear='docker builder prune'
alias dsize='docker system df'
alias dup='docker compose up -d'
alias ddown='docker compose down'
alias drunpython='docker run -d python:3.10 python -c "import time; time.sleep(1000000)"'

## Airflow
export AIRFLOW_HOME=~/airflow
export AIRFLOW__CORE__LOAD_EXAMPLES='false'
# alias adl='rm -rf ~/airflow/dags/* ; find ~/Desktop/Airflow/mwaa/dags -type f -name "*.py" -exec ln -s -t ~/airflow/dags/ {} + &> /dev/null; airflow dags list'
alias af='docker exec -it aws-mwaa-airflow-triggerer-1 bash -c "airflow dags reserialize"'
alias adl='rm -rf ~/airflow/dags/* ; ln -s ~/Desktop/Airflow/mwaa/dags/* ~/airflow/dags/ ; airflow dags list'
alias adli='airflow dags list-import-errors'
# Convert this to zsh: find ~/Desktop/Airflow/mwaa/dags -type f -name "*.py" -exec ln -s -t ~/airflow/dags/ {} + &> /dev/null;

## AWS
alias sid='python3 -c "from datetime import datetime; print(f\"Stmt{int(datetime.now().timestamp()*1000)}\", end=\"\")" | pbcopy'

# Functions
## Go to the parent directory of a file if the paramete is a file not folder
function CD() {
  if [ -f $1 ]; then
    parent_dir=$(dirname $1)
    cd $parent_dir
  elif [ -d $1 ]; then
    cd $1
  fi
}

## Repo
function buka() {
  if [ $1 = "ab" ]; then
    code ~/Desktop/alpha-beta
  elif [ $1 = "cd" ]; then
    code ~/Desktop/cat-dog
  fi
}

echo -e $REMINDER
complete -C ~/bin/terraform terraform
