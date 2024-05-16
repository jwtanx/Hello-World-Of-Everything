# S3

## Syncing
- To include *.sh files only, the order is important because if you put --include first then only --exclude "*", all files will be excluded
- Directory
```sh
local-test
├── foo
│   ├── bye.sh
│   └── dont-copy.txt
└── hello.sh
```
Commands
```sh
aws s3 sync local-test/ s3://test-bucket/test --dryrun --exclude "*" --include "*.sh"
```
Output
```sh
# Output: Dryrun is just testing what is the final expected sync
(dryrun) upload: local-test/foo/bye.sh to s3://test-bucket/test/foo/bye.sh
(dryrun) upload: local-test/hello.sh to s3://test-bucket/test/hello.sh
# To upload the files, remove the --dryrun flag
```