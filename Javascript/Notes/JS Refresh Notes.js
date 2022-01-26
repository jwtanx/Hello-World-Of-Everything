// This is a comment, the comment starts with double forward slash

/*
This is a multi-lines comment
This is the second line of the comment
*/

// Install NODE JS here: https://nodejs.org/en/download/
// then type `node` in the terminal to start coding

// ========================================================================== //

// < EXPORTING THE FUNCTION TO BE CALLED IN THE TERMINAL > //
module.exports.myFunction = function () {
  // Initializing the variable
  var a = 120;
  // Printing the variable a's value to the console
  console.log(a);
};

/* 
How to call this function "myFunction" in the terminal?
https://stackoverflow.com/questions/30782693/run-function-in-script-from-command-line-node-js/36480927

For example the current filename is "abc.js"
1. Open up your terminal and type the below codes
2. node
3. var tester = require("./abc")
4. tester.myFunction()

It will output `120`

# One liner in the terminal
node -e 'require("./abc").myFunction()'
*/

// < VARIABLES : CONST (CONSTANT) > //
// Define 'fruit' as a constant and give it the value 'apple'
const fruit = "apple";
console.log("My favorite fruit is: " + fruit);

// Uncaught TypeError: Assignment to constant variable
fruit = "banana";

// Uncaught SyntaxError: Identifier 'fruit' has already been declared
const fruit = "banana";

// < ARRAY : BASICS > //
// Declaring
var fruits = [];
const books = [];

// Initializing
var fruits = ["watermelon", "apple", "orange"];

// < MATHS : RANDOM > //
Array.prototype.choice = function () {
  return this[Math.floor(Math.random() * this.length)];
};

var fruits = ["watermelon", "apple", "orange"];
console.log(fruits.choice());

// Another method
// https://stackoverflow.com/questions/4550505/getting-a-random-value-from-a-javascript-array
const random = Math.floor(Math.random() * months.length);
console.log(random, months[random]);
