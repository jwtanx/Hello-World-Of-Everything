# Bazel

## WORKSPACE

## Rules

## filegroup
```
filegroup(
  name = "dir1",
  srcs = glob(["dir/**"]),
)
```

## Glob
### Excluding files
https://bazel.build/reference/be/functions#glob_example

## pkg_tar
https://www.reddit.com/r/bazel/comments/un2e0b/copying_a_directory_in_a_tar_file_is_a_nightmare/

### Saving all files into pkg_tar
https://stackoverflow.com/questions/63889189/copy-a-directory-to-a-new-directory-in-bazel
```python
filegroup(
    name = "src_files",
    srcs = glob([
        "src/**",
    ]),
)

pkg_tar(
    name = "pack_srcs",
    extension = "tar.gz",
    srcs = [":src_files"],
)

genrule(
    name = "unpack_to_dist",
    srcs = [":pack_srcs"],
    outs = ["dist"],
    cmd = "mkdir $(RULEDIR)/dist && tar -C $(RULEDIR)/dist -zxvf $(SRCS)"
)
```

### Strip prefix
https://stackoverflow.com/questions/54681716/how-to-create-a-directory-structure-in-bazel

This is required to avoid the file in the pkg_tar got flattened and de-duplicated