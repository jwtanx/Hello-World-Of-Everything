# Commands for Git

## Initialization / First setup
1. The very first step of creating a new git repo
```git init```

2. Adding files to the staging area (Staging the new / changed files)
- To be done before committing
```git add .```
- The `.` here means the current directory

3. Commiting the changes with a descriptive message
```git commit -m "First commit"```

> Publishing / Pushing to Github steps will be listed below

## Staging & Unstaging
1. Adding files to the staged ares (Staging)
```git add <file>```
- Replace the `<file>` with `.` to add the whole directory to the staging area

2. Unstage the staged file before committing
```git restore --staged <file>```

## To discard any changes of the file
```git restore <file>```
- For newly created files, delete manually, you cannot discard the newly created files using this command

## Check the gloval configuration
```git config --global --list```

## Checking the changes
1. Get the log of the addition or deletion of the files
```git log --raw```

2. List of the flow of the log
```git reflog```

3. Get the difference between two commits
    1. Find the git commit id first
    ```git log --raw```
    2. Copy the first few letter of the commit id (for e.g. c28jkmxc9) you would like to compare with
    3. Git diff the one with the current status
    ```git diff c28jkmxc9 .```
       - `.` here means the current status

## Reverting the commit (There is no uncommit)
[Reference](https://www.theserverside.com/tutorial/How-to-git-revert-a-commit-A-simple-undo-changes-example)
It is not same as reset, `git revert` will just revert the changes for the commit you want. But `git reset` will reset everything and back to the commit point.
> When you git revert a commit, only the changes associated with that commit are undone. Cumulative changes from subsequent commits aren't affected. If you wish to undo every change since a given commit occurred, you'd want to issue a hard git reset, not revert.
```git revert c5fbed32f7```
Once you revert, the added files / changes for the commit will be reverted, added files will be removed.

## Hard reset to a commit checkpoint (Lesser confusion)
- It is like a time machine, Windows' system restore. But be careful, all the files from the point onwards will be removed, uncommit files will be removed too.
```git reset c5fbed32f7```
- But if there is uncommit tracked files you would like to keep, use `git stash`, the untracked file seem to be no affected.

## Keeping uncommited file before resetting
```git stash```
- This will save all the uncommited but tracked files into a stash, after you reset to a checkpoint, you can `git stash pop` it back and continue working.
```git stash pop```

## Hard reset to undo the tracked files that has changes
```git reset --hard```

## Git clean to remove all the untracked files
```git clean -fxd```

## Branch
1. Creating a new branch
> Note: Before you can create a branch, make sure you have your first commit to your main branch / master branch
```git branch feature-1```
> Note: The new branch created will based on the current branch you are on, meaning the files will be the same as the current branch.

1. Checking the list of the branches
```git branch```

1. Switching branch to work on
```git checkout feature-1```

1. Deleting a branch
```git branch -d feature-1```
When you are in the branch, you need to checkout to another branch first before you can delete this branch.

1. Create a new branch and checkout into it directly
```git checkout -b <new_branch_name>```
> Note: The new branch created will based on the current branch you are on, meaning the files will be the same as the current branch.

## Merging between two branch (Without remote and no pull request needed, locally)
1. Checkout to the feature branch you are done working on
```git checkout feature-1```

2. Merge the code in the main / dev branch into your feature branch to check any conflicts.
```git merge dev```
- Think it like merging codes from `dev` branch to `feature-1` branch

1. Solve the conflicts if there is any and make changes again

2. Update the main / dev branch with the updated merged feature-1 branch
```git checkout dev```
```git merge feature-1```
- Think it like merging codes from `feature-1` branch to `dev` branch

---

## Remote (GitHub) [Researching...]
1. Setting up the upstream remote

2. Viewing the remote url
```git remote -v```

## Merging the feature branch into the main branch steps (From remote for pull request)
1. Checkout to the main / dev branch
```git checkout dev```

2. Check and update the branch if there is updates
```git pull```

3. Checkout back into the branch that you want to merge into the main branch
```git checkout feature-1```

4. Merge the updates from dev branch into your feature branch before you push your branch for later pull request confirmation
```git merge dev```
- Think it like merging codes from `dev` branch

5. Push the merged feature branch to the remote
```git push```
- From GitHub side, you can request for pull request, then the project leader will check and accept the pull request.
- When the pull requet is accepted, the codes in your feature branch will be merged into the main / dev branch.


## Alias
1. Checking the list of the alias
```git config --get-regexp '^alias\.'```
```sh
alias.st status
alias.a add
alias.b branch
alias.c commit
alias.co checkout
alias.cob checkout -b
alias.alias config --get-regexp '^alias\.'
alias.rv remote -v
alias.ac !git add -A && git commit -m
```

2. Setting a new alias
```git config --global alias.ac '!git add -A && git commit -m'```
- Next time when adding **ALL** the newly changes files while adding commit message, just type: `git ac "Added sleeping mode"`
- [Reference](https://stackoverflow.com/questions/4298960/git-add-and-commit-in-one-command)

### Some useful aliases
| Alias                       | Setting up                                                  | Description                                                        |
| --------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------ |
| `git st`                    | `git config --global alias.st status`                       | Getting the current status of the branch                           |
| `git co <branch_name>`      | `git config --global alias.co checkout`                     | Checkout to the other branch                                       |
| `git cob <new_branch_name>` | `git config --global alias.cob checkout -b`                 | Create a new branch and checkout to the newly created branch       |
| `git ac "mesage"`           | `git config --global alias.ac !git add -A && git commit -m` | Adding all the changes / untracked files and commit with a message |

## Rebase
- `git rebase master`: Update the current branch with the code from the master branch
- `git rebase old-changes`: Make sure you are at the new feature branch that is depending on `old-changes`: the `new-changes` branch will be updated with the `old-changes` feature below it
- `git rebase old-changes new-changes`: Rebase `old-changes` branch with `new-changes` branch, place `new-changes` on top of `old-changes` branch
- Merge the conflict manually and then `git rebase --continue`
- Merging the conflict is a very tedious work, might as well just copy the file to the point of the change log where you want to add the new changes

### GERRIT: Rebasing a patch
# Go to the branch you are working on and pull the latest patch
git pull https://username@gerrit.domain.com/a/demo/hello_world refs/changes/08/22308/<new-patch-#> --rebase

# Add new files and commit the new change
git commit --amend


## Git Fork
1. Checking the list of branches
```sh
git branch -a
# remotes/origin/feature-a
```

2. Git clonning the specific branch
Reference: https://www.freecodecamp.org/news/git-clone-branch-how-to-clone-a-specific-branch/
```sh
git clone --branch <branchname> <remote-repo-url>
git clone -b <branchname> <remote-repo-url>
git clone -b feature-a https://jwtanx@github.com/jwtanx/Hello-World-Of-Everything
```

3. Pulling the latest patch for your forked repo from the original repo
Reference: https://levelup.gitconnected.com/how-to-update-fork-repo-from-original-repo-b853387dd471
```sh
# Adding the upstream remote first (Original repo remote url)
git remote add upstream <original repo>

# Pulling from the upstream main branch
git pull upstream master

# Rebase the fetched patches to your own main branch
git rebase upstream/main

# Push to your own forked repo
git push -f origin master
```

## Remote
### Change remote link
```sh
git remote set-url origin https://jwtanx@github.com/new-repo-name
git remote set-url origin  $(echo $(git config --get remote.origin.url) | sed 's/old-domain/new-domain/g')
```