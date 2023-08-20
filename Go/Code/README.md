# Golang Cheat Sheet

## Basic
```go
package main

import "fmt"

func main() {
    fmt.Println("Hello")
}
```

## Printing
Three methods of printing out some string
```go
// Must import fmt built-in library
import "fmt"

func main() {
    // Method 1: Normal printing, does not skip to the next line for the next print
    fmt.Print("Hello")

    // Methdo 2: Print and add a new line beneath
    fmt.Println("This is still in the first line due to the fmt.Print() above")
    fmt.Println("This is the second line")

    // Method 3: Print with formatting
    name := "Jeff"

    // There is no new line created like fmt.Print too, we can add the `\n` to the next line
    fmt.Printf("My name is %s\n", name)
    
}
```
### Printing Formats
| Format | Description                                     |
| ------ | ----------------------------------------------- |
| `%s`   | String                                          |
| `%d`   | Integer                                         |
| `%g`   | Float                                           |
| `%t`   | Boolean                                         |
| `%T`   | Type                                            |
| `%b`   | Base 2 numbers                                  |
| `%o`   | Base 8 numbers                                  |
| `%O`   | Base 8 numbers with 0o prefix                   |
| `%d`   | Base 10 numbers with lower-case letters for a-f |
| `%x`   | Base 16 numbers with upper-case letters for A-F |
| `%X`   | Base 16 numbers                                 |
| `%g`   | Float values                                    |
| `%s`   | String values                                   |
| `%e`   | Scientific values                               |

## Variables
The data type in Golang is fixed, it is not like Python where you can reassigned a variable with any data type

1. Initialization
```go
// Purely initializing without setting a value
var name string

// This works too without the data type
var age

// Adding value to it
name = "John"
age = 123
```

2. Quick declaration (initialize + setting value)
```go
// Simplest declaration
name := "John"

// Reassigning the value
name = "John Cena"
```
The variable `name` can be reassigned with data with the same data type only

3. The perfectionist method
```go
// More precise variable declaration
var name string = "John"
var age = 55
name = "John Cena"
age = 69
```
The variable `name` with the declaration of `string` beside it means that the variable data type is fixed

4. Declaring variable outside of function body
```go
// Reference: https://www.geeksforgeeks.org/different-ways-to-find-the-type-of-variable-in-golang/
package main

import "fmt"

name := "Jeff" // This will throw an error (syntax error: non-declaration statement outside function body)
var name string // Method 1: Works
var name = "John" // Method 2: Works

func main() {
    name = "Jeff"
    fmt.Println("My name is", name) // Output: My name is Jeff
    fmt.Println("My name is" + name) // Output: My name isJeff <-- note that there is no space
}
```

## Data type
Getting the type of the variable
```go
import (
    "fmt"
    "reflect"
)

func main() {
  
    // string type
    var1 := "hello world"
  
    // integer
    var2 := 10
  
    // float
    var3 := 1.55
  
    // boolean
    var4 := true
  
    // shorthand string slice declaration
    var5 := []string{"foo", "bar", "baz"}

    // string array declaration
    var6 := [3]string{"foo", "bar", "baz"}
  
    // map is reference datatype
    var7 := map[int]string{100: "Ana", 101: "Lisa", 102: "Rob"}
  
    // complex64 and complex128 is basic datatype
    var8 := complex(9, 15)
  
    // using %T format specifier to determine the datatype of the variables
    fmt.Println("Using Percent T with Printf")
    fmt.Printf("var1 = %T\n", var1) // var1 = string
    fmt.Printf("var2 = %T\n", var2) // var2 = int
    fmt.Printf("var3 = %T\n", var3) // var3 = float64
    fmt.Printf("var4 = %T\n", var4) // var4 = bool
    fmt.Printf("var5 = %T\n", var5) // var5 = []string 
    fmt.Printf("var6 = %T\n", var6) // var6 = [3]string
    fmt.Printf("var7 = %T\n", var7) // var7 = map[int]string
    fmt.Printf("var8 = %T\n", var8) // var8 = complex128
  
    // using TypeOf() method of reflect package to determine the datatype of the variables
    fmt.Println("Using reflect.TypeOf Function")
    fmt.Println("var1 = ", reflect.TypeOf(var1)) // var1 =  string
    fmt.Println("var2 = ", reflect.TypeOf(var2)) // var2 =  int
    fmt.Println("var3 = ", reflect.TypeOf(var3)) // var3 =  float64
    fmt.Println("var4 = ", reflect.TypeOf(var4)) // var4 =  bool
    fmt.Println("var5 = ", reflect.TypeOf(var5)) // var5 =  []string
    fmt.Println("var6 = ", reflect.TypeOf(var6)) // var6 =  [3]string
    fmt.Println("var7 = ", reflect.TypeOf(var7)) // var7 =  map[int]string
    fmt.Println("var8 = ", reflect.TypeOf(var8)) // var8 =  complex128
  
    // using ValueOf() method of reflect package to determine the value of the variable
    // Kind() method returns the datatype of the value fetched by the ValueOf() method
    fmt.Println("Using reflect.ValueOf.Kind() Function")

    fmt.Println("var1 = ", reflect.ValueOf(var1).Kind()) // var1 =  string
    fmt.Println("var2 = ", reflect.ValueOf(var2).Kind()) // var2 =  int
    fmt.Println("var3 = ", reflect.ValueOf(var3).Kind()) // var3 =  float64
    fmt.Println("var4 = ", reflect.ValueOf(var4).Kind()) // var4 =  bool
    fmt.Println("var5 = ", reflect.ValueOf(var5).Kind()) // var5 =  slice
    fmt.Println("var6 = ", reflect.ValueOf(var6).Kind()) // var6 =  array
    fmt.Println("var7 = ", reflect.ValueOf(var7).Kind()) // var7 =  map
    fmt.Println("var8 = ", reflect.ValueOf(var8).Kind()) // var8 =  complex128
}
```
| Type      | Deccription                                   | Declaration                                                     | Example value                   |
| --------- | --------------------------------------------- | --------------------------------------------------------------- | ------------------------------- |
| `string`  | Words, sentence                               | `name := "John Cena"`                                           | `"John Cena"`                   |
| `int`     | Number, integer                               | `year := 1999`                                                  | `1999`                          |
| `float64` | Decimal number                                | `pi := 3.142`                                                   | `420.00000069`                  |
| `bool`    | True or false                                 | `isChecked := true`                                             | `true`, `false`                 |
| `array`   | List with fixed size                          | `nums := [3]int{10,20,30}`                                      | `[10 20 30]`                    |
| `slice`   | List that can grow / shrink in size           | `students := []string{"Ali", "Abu", "Muthu"}`                   | `[Ali Abu Muthu]`               |
| `map `    | Like Python's dictionary with a key and value | `prices := map[string]int{"orange": 5, "apple": 3, "lemon": 4}` | `map[apple:3 lemon:4 orange:5]` |

## Functions
DRY: Don't Repeat Yourself
```go
// Main function
func main() {
	shoutPizza() // Pizza!
	fmt.Println(getPizza()) // Your pizza is served
	fmt.Println(getPizzaWithName("Salmon Blazing"))
}

// Normal function just to process something like Java's void function: This will not return any value
func shoutPizza() {
    fmt.Println("Pizza!")
}

// Function returning value
func getPizza() string { // <-- data type is required to tell 
    return "Your pizza is served"
}

// Function with paraneters
func getPizzaWithName(pizzaName string) string {
    return pizzaName + " Pizza"
}
```

## Data Structures
### Array: Fixed number of elements
- Every element in the array must of the same data type

#### One Dimensional Array
```go
// Initialization
var numbers [5]int
fmt.Println(nunmbers)
// Output: [0 0 0 0 0]
// Indexes: 0 1 2 3 4

// Assign values
numbers[4] = 100
fmt.Println(numbers)
// [0 0 0 0 100]

fmt.Println(numbers[4])
// 100

fmt.Println(len(numbers))
// 5

// Direct declaring an array like a tuple
fibs := [5]int{1, 1, 2, 3, 5}

fibs[5] = 100 // Cannot because `index out of bound`, once you have set the initial size of the array, you cannot grow / shrink the size of the array anymore, max index is from 0 to 4 for an array with size 5

```

#### Two Dimensional Array
```go
var twoDimArray [2][3]int
fmt.Println(twoDimArray)
// [[0 0 0] [0 0 0]]

// For loop: More example will be shown in the following section
for i := 0; i < len(twoDimArray); i++ {
    for j := 0; j < len(twoDimArray[0]); j++ {
        twoDimArray[i][j] = i + j
    }
}
fmt.Println(twoDimArray)
// [[0 1 2] [1 2 3]]
```

### Slices: Array but the size can grow / shrink
- Every element in the slice must of the same data type
```go
// Declaration
names := []string{"John", "Karen", "Smith"}

// Adding a new name, the names is reassigned with a new object rather than the new element getting appended into the original slice
names = append(names, "Cena")

fmt.Println(names)
// [John Karen Smith Cena]

```

## Loops
Mainly for looping through an array, slice or a map
```go
names := [3]string{"Ali", "Abu", "Muthu"}

// Method 1: Most basic for loop like Java
for i := 0; i < len(names); i ++ {
    fmt.Println(names[i])
}
/*
Ali
Abu
Muthu
*/

// Method 2: enumerate through the array
for i, name := range names {
    fmt.Println(i, name)
}
// The := in the for loop is only used to declare the i and the name once
// You need to redeclare the variable if you are using it outside of the loop
/*
0 Ali
1 Abu
2 Muthu
*/

// The bottom code produce an error because the variable `i` is not used
// Error: i declared and not used
for i, name := range names {
    fmt.Println(name)
}

// To solve this, use a blank variable
for _, name := range names {
    fmt.Println(name)
}

```