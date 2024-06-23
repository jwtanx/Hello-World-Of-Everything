# S3

## Login first
```sh
aws sso login
```

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
aws s3 sync local-test/ s3://jw-test-bucket-123/test --dryrun --exclude "*" --include "*.sh"
```
- `--dryrun`: to check the list of files that will be uploaded / downloaded / deleted
- remove the --dryrun flag to actually sync the files

Output
```sh
# Output: Dryrun is just testing what is the final expected sync
(dryrun) upload: local-test/foo/bye.sh to s3://jw-test-bucket-123/test/foo/bye.sh
(dryrun) upload: local-test/hello.sh to s3://jw-test-bucket-123/test/hello.sh
# To upload the files, remove the --dryrun flag
```

Condition:
- When the modified date of the file is different, it will be uploaded
- When the file is not in the destination, it will be uploaded
- When the file is in the destination but not in the source, it will not be deleted
  - How to fix?
  - Use `--delete` flag to delete the files that are not in the source
    ```
    aws s3 sync local-test/ s3://jw-test-bucket-123/test --dryrun --delete --exclude "*" --include "*.sh"
    (dryrun) upload: local-test/foo/bar/new.sh to s3://jw-test-bucket-123/test/foo/bar/new.sh
    (dryrun) upload: local-test/foo/bye.sh to s3://jw-test-bucket-123/test/foo/bye.sh
    (dryrun) delete: s3://jw-test-bucket-123/test/hello.sh
    ```
- When the include flag changes to .txt, the .sh files are not deleted eventhough we have the --delete flag
  ```sh
  aws s3 sync local-test/ s3://jw-test-bucket-123/test --dryrun --delete --exclude "*" --include "*.txt"
  (dryrun) upload: local-test/foo/dont-copy.txt to s3://jw-test-bucket-123/test/foo/dont-copy.txt
  ```
- But if you include the .sh files, the .sh files which was deleted on your local will be deleted on the S3
  ```sh
  aws s3 sync local-test/ s3://jw-test-bucket-123/test --dryrun --delete --exclude "*" --include "*.txt" --include "*.sh"
  (dryrun) upload: local-test/foo/dont-copy.txt to s3://jw-test-bucket-123/test/foo/dont-copy.txt
  (dryrun) upload: local-test/foo/bar/new.sh to s3://jw-test-bucket-123/test/foo/bar/new.sh
  (dryrun) upload: local-test/foo/bye.sh to s3://jw-test-bucket-123/test/foo/bye.sh
  (dryrun) delete: s3://jw-test-bucket-123/test/hello.sh
  ```

### Syncing to local
- To sync from S3 to local, use the following command
  ```sh
  aws s3 sync s3://jw-test-bucket-123/test local-test --dryrun --exclude "*" --include "*.sh"
  (dryrun) download: s3://jw-test-bucket-123/test/foo/bye.sh to local-test/foo/bye.sh
  (dryrun) download: s3://jw-test-bucket-123/test/hello.sh to local-test/hello.sh
  ```