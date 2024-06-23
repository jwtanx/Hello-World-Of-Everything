# Vault Agent
function get() {
  list=("aws" "gh")
  if [ -z $1 ]; then
  elif [[ " ${list[@]} " =~ " ${1} " ]]; then
    sudo zsh -c "source ~/vault.sh ; get $1"
  fi
}