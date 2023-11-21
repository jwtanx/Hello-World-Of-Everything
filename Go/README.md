# Golang

### Jump into [Code Cheat Sheet](Code/README.md)

## Installation
1. Head to the link: https://go.dev/dl/
2. Choose the operating system and download it
3. Verify by typing `go version` in terminal or cmd
4. Using VS Code, in the extension tab, install Go extension by Go Team at Google and enable it
5. Create a new folder and a new file say `main.go`, you will see a recommendation by VS Code, click install with the extra tools
6. Done

## Basics
Create a new file named `main.go`
```go
// Package declaration
package main

// Import other packages that we need
import "fmt"

// Declare functions
func main() {
	fmt.Println("Hello")
}
```
### Understanding the fundamentals
1. `package` == Project == Workspace
   - Each of the go file should start with a `package xxx`, the package where it belongs to
   - Two types:
     - Executable: An executable file is generated for us to run, the name of the file has to be `main.go` only then it can be built into an executable file. If you name it into some other file name, it cannot be built. Also, remember it must have a function call `main` as well.
     - Reusable: Reusable functions in a package to be imported across the project, they are code dependencies, the code that we are relying on. Setting a package name other than `main`
     - List of packages / standard libraries of GO can be found: https://pkg.go.dev/std
2. `import`
   - In the code, the `fmt` is imported, it is a built-in go package which stands for format.
   - `fmt` is a standard library where we can use it to print something on the terminal
   - `import` keyword is mainly used to include the reusable packages
3. `func` = function

## Go Commands
### `go run`: Compile one or two files and execute
```bash
go run main.go
```
- You will then see a "Hello" on the terminal
- We can also run multiple files: `go run main.go script.go` | `go run script.go main.go`
```go
// script.go
// Just need to make sure both scripts are in the same package
package main

import "fmt"

func greet() {
   fmt.Println("Hello there!")
}
```
```go
// main.go
// Just need to make sure both scripts are in the same package
package main

func main() {
   greet() // Hello there!
}

```

### `go build`: Compiles files only
```bash
go build main.go

# Then a main executable will be created, to run it, do:
./main
```

### `go fmt`: Format all the code
```bash
cd helloworld
go fmt
```

### `go install`: Compile and install a package

### `go get`: Download raw source code of someone's package

### `go test`: Run test on the current project
Note: Need to run `go mod init` once, or else error: `go: go.mod file not found in current directory or any parent directory; see 'go help modules'`
- File name of the must be suffix with `_test.go`
- To run all test in the package, run `go test`
- Example of a test file: `deck_test.go`
```
package main

import "testing"

// We will tell the variable t here if something went wrong
func TestNewDeck(t *testing.T) {
	cards := newDeck()
	totalDeckCards := 52
	if len(cards) != totalDeckCards {
		t.Errorf("Expected deck leng of %v, but got %v", totalDeckCards, len(cards))
	}
}
```

### `go mod init`: Initialize the workspace
This is required before you ca run go test
```bash
# Example 1
go mod init example.com/a

# Example 2
go mod init cards
```

#### Creating a workspace
- https://go.dev/doc/tutorial/workspaces

### `go mod tidy`: Update / adding module requirements and checksum

### `go list`

## FAQs
### 1. Is there Virtual Environment like Python's?
There is only `go.mod` file to act like the requirements file in Python and there is no virtual environment like Python, Go has its own dependencies settled by `go.mod` file [using go module](https://go.dev/blog/using-go-modules)
