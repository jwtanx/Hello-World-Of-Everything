# Note: pbcopy is in macOS, so it won't work in Ubuntu.
# If ubuntu: Replace pbcopy with xclip -sel clip

alias out='function get() {}'

function get() {
  if [ $1 = "aws" ]; then
    echo -n "AWS_TOKEN" | pbcopy
    out
  elif [ $1 = "gh" ]; then
    echo -n "GITHUB_TOKEN" | pbcopy
    out
  else
  fi
}