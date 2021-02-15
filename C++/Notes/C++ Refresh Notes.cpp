/* BASICS OF C++
========================================
Last updated: Mon, February 15, 2021 - 16:58

NOTE: This file is not compilable, I use the #define to highlight the syntax while writing the notes
*/

/* HELLO WORLD
========================================*/
#include <iostream>

using namespace std;

int main() {
    cout << "Hello World" << endl;
    return 0;
}

/* PRINTING
========================================*/
#define cout "Normal_Printing"
cout << "1";
cout << "2";
cout << "3";
// Output: 123

#define next_Line "With 'endl;' or '\n' behind"
cout << "1" << endl;
cout << "2\n";
cout << "3" << endl;
/* Output:  1
            2
            3
*/

#define cout "Printing Variable";
memer = "Jeff";
cout << "My name is " << memer << "! POG!" << endl;

/* VARIABLES & DATA TYPES
========================================*/
#define String "Assigning"
string text = "This is a sentence"; // Make sure it is double quote

#String Length
cout << text.length(); // 18

#String Array
cout << text[8]; // a

#String Array Amendment
text[8] = 'A';
cout << text; // This is A sentence

#String Find Index: Find the very first index of the word
// str.find(TO_FIND, STARTING_INDEX)
text = "This is A sentence"
cout << text.find('e', 11); // 11
cout << text.find("e", 11); // 11
cout << text.find('e', 12); // 14
// NOTE: Without the STARTING_INDEX, it will start finding from the index 0

#String Substring
// str.substr(STARTING_INDEX, NUMBER_OF_CHAR_TO_GRAB)
text.substr(8); // A sentence
text.substr(8, 5); // A sen

#String Replacing
// str.replace(STARTING_INDEX, NUMBER_OF_CHAR_BEHIND_TO_REPLACE, REPLACE_WITH);
text.replace(10, -1, "replacement"); // This is A replacement
text.replace(10, 0, "new "); // This is A new sentence
text.replace(10, 3, "new"); // This is A newtence

=======
#define Integer "Assigning"
int age = 22;

=======
#define Float "Used on specific occasion"
float price = 12.99;

=======
#define Double "Can store more decimal point than float"
double pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286;

=======
#define Character
char grade = 'F'; // Make sure it is single quote

=======
#define Boolean
bool paid = true;
bool ate = false;

// NOTE: You can initialize both variable at the same time
int a = 5, b = 6;
float a, b;

/* ARRAYS
========================================*/
#define Arrays "Assigning"
int nums[] = {2, 1234, 542, 312, 12};
int[] nums = {2, 1234, 542, 312, 12}; // int[] - This will not work in C++ but will work in Java
double price[] = {2.99, 1.12, 542.22, 2.23, 5.9};
string name[] = {"Abu", "John", "Mendy", "Jeff"};

// NOTE: All index starts from 0
cout << nums[0]; // 2
cout << nums[99]; // 0
cout << price[3]; // 2.23
cout << name[4]; // Nothing will be printed

=======
#define Arrays "Setting the arary size"
int num[10] = {5, 2, 1, 2, 3}; // <-- Setting an array of integers that store 10 elements
cout << num[10]; // 0
cout << num[9]; // 0

=======
#define Arrays "Changing the data in the array"
int num[] = {5, 3, 2, 1};
num[0] = 4;
cout << num[0]; // 4
cout << num; // 0x61fde0 <- The location of the address that store the array

=======
#define Arrays "Printing the elements of the array"
// Reference: https://www.techiedelight.com/print-contents-array-cpp/

#Array_Printing "For Loop: Using array indices"
int num[] = {1,2,3,4,5};

cout << sizeof(num); // 20

for(int i = 0; i < sizeof(num) / sizeof(num[0]); i++){ 
	// NOTE: The reason why need to divide by the size of num[0] is because in an array, every element has a equal size
	// Take a look at Computer System and Architecture
	cout << i; // 12345
}

// Using size_t: size_t is the type returned by the sizeof operator and is widely used in the standard library to represent sizes and counts.
// Reference: http://www.cplusplus.com/reference/cstring/size_t/
int input[] = { 1, 2, 3, 4, 5 };
size_t n = sizeof(input)/sizeof(input[0]);

// loop through the elements of the array
for (size_t i = 0; i < n; i++) {
    cout << input[i] << ' ';
}

#Array_Printing "Using copy & experimental::ostream_joiner"
int input[] = { 1, 2, 3, 4, 5 }; 
std::copy(std::begin(input), std::end(input), std::experimental::make_ostream_joiner(std::cout, " "));
// NOTE: Only applicable for C++ 17

#Array_Printing "Range based for loop"
int num[] = { 1, 2, 3, 4, 5 };
 
for (const auto& i: num) {
    cout << i << ' '; // 1 2 3 4 5
}

// Simplest way to print an array
for (auto i: num){
	cout << i; // 12345
}

#Array_Printing "Iterators"
int num[] = { 1, 2, 3, 4, 5 };

for(auto i = cbegin(num); i != cend(num); i++){
	cout << *i << endl;
}
// NOTE: If without the * in the '*i', the output would be the address for each element in the array

#Array_Printing "For_each"
#include <iostream>
// #include <vector> // This is not needed also can run
#include <algorithm> // This is a must
 
using namespace std;
 
void print(const int &i) {
    cout << i << ' ';
}
 
// Print contents of an array in C++ using for_each
int main()
{
    int input[] = { 1, 2, 3, 4, 5 };
    for_each(begin(input), end(input), print);
    return 0;
}

#Array_Printing "For_each: Better using lamdba as compared to the above"
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Print contents of an array in C++ using std::for_each
int main() {
    int input[] = { 1, 2, 3, 4, 5 };
 
    for_each(begin(input), end(input), [](const int &e) {
    	cout << e << " ";
    });
 
    return 0;
}

/* OPERATORS
========================================*/
#define Arithmetic_Operators "Maths"
/*
a + b   : Adds a and b
a - b   : Subtracts b from a
a * b   : Multiplies a and b
a / b   : Divides a by b
a % b   : The remainder part of the integer division of a by b
a++		: Adding 1 to 'a'
a--		: Substract 1 from 'a'
*/
int a = 10, b = 3;
cout << a + b << endl; // 13
cout << a - b << endl; // 7
cout << a * b << endl; // 30
cout << a / b << endl; // 3
cout << (float) (a / b) << endl; // 3
cout << ((float) (a) / (float)(b)) << endl; // 3.33333
cout << 10.0 / 3 << endl; // 3.33333
cout << 10 / 3.0 << endl; // 3.33333
cout << 10.0 / 3.0 << endl; // 3.33333
cout << a % b << endl; // 1

a = 10;
cout << a << endl;   // 10
cout << a++ << endl; // 10
cout << a << endl;	 // 11
// NOTE: for a++, the 'a' will be printed first then the it only increased by 1

a = 10;
cout << a << endl;   // 10
cout << ++a << endl; // 11
cout << a << endl;   // 11
// NOTE: for ++a, the 'a' is incresed by 1 before being printed

=======
#define Assignment_Operators "Direct Assigning"
/*
x = 1   : x = 1
x += 2  : x = x + 2
x -= 3  : x = x - 3
x *= 4  : x = x * 4
x /= 5  : x = x / 5
x %= 6  : x = x % 6
*/

=======
#define Logical_Operators "Boolean"
bool x = true, y = false;
// NOTE: C++ make the true value to 1 while the false value to 0

cout << x; // 1
cout << y; // 0

/*
and : True when both operands are True
or  : True when one of the operands is True
not : True when the operand is False [Negation/Opposite of the operand]
Precedence: not > and > or
*/

cout << x and y; // 0
cout << x or y; // 1
cout << not x; // 0

// Same thing below
cout << x && y; // 0
cout << x || y; // 0
cout << !x; // 0
// NOTE: The &&, ||, ! is noramlly use for if-else

=======
#define Comparison_Operators "Comparing between/among variables"
int x = 5, y = 2;
cout << (x == y); // Output: 0
cout << (x != y); // Output: 1
cout << (x < y);  // Output: 0
cout << (x > y);  // Output: 1
cout << (x <= y); // Output: 0
cout << (x >= y); // Output: 1
// NOTE: 1 == true; 0 = false;

// Special feature like python
int x = 1, y = 2, z = 3;
cout << (x < y < z);    // Output: 1

int x = 1, y = 3, z = 3;
cout << (x > y == z);   // Output: 0

/* LIBRARIES
========================================*/
#define <cmath> "Mathematics Library"

#include <iostream>
#include <cmath>

using namespace std;

int main() {

	cout << pow(2, 5) << endl; // 2 to the power of 5 = 32
	cout << sqrt(36) << endl; // squaroot of 36 = 6
	cout << round(4.35) << endl; // 4
	cout << round(4.45) << endl; // 4
	cout << round(4.55) << endl; // 5
	cout << ceil(4.1) << endl; // 5
	cout << floor(4.9) << endl; // 4
	cout << fmax(3, 10) << endl; // 10 <- Return the largest number
	cout << fmin(3, 10) << endl; // 3 <- Return the smallest number

	// NOTE: More functions like sin(rad), cos(rad), tan(rad), exponential
	// NOTE: Make sure that the sine, cos, tan parameter are in radian
	// Convert degree to radian first, M_PI is given in the C++
	double degree = 90;
	double rad = (degree / 180) * M_PI;
	cout << sin(rad) << endl; // 1.22461e-16 == 0
	cout << cos(rad) << endl; // -1
    cout << tan(rad) << endl; // -1.22465e-16 == 0
    cout << exp(2) << endl; // e^2 = 7.38906

	return 0;
}

/* GETTING USER INPUTS
========================================*/
#define Input "Getting int, float, double, char"

#include <iostream>

using namespace std;

int main() {

	int age;
	cout << "Enter your age: ";

	// Getting the user input
	cin >> age;
	// NOTE: Make sure the double arrows are pointing to the age

	cout << "You are " << age << " years old.";

}

=======
#define Input "Getting two or more variables at the same time"
int a, b;
cout << "Enter two numbers separated by a space: ";
cin >> a >> b;
cout << "The answer is " << a + b;

/*
Enter two numbers separated by a space: 5 7
The answer is 12
*/

=======
#define Input "Getting string"
// getline(cin,  STR_VARIABLE);

string address;
cout << "Enter your address: ";
getline(cin, address);
cout << "Output: " << address;

/*
Enter your address: 1, Meme Street CO 10521.
Output: 1, Meme Street CO 10521.
*/

// NOTE: If you are not using getline(cin, STR_VARIABLE);
string sentence;
cout << "Enter your sentence: ";
cin >> sentence;
cout << "Output: " << sentence;

/*
Enter your sentence: Testing this is a test.
Output: Testing
*/

/* FUNCTION
========================================*/
#include <iostream>

using namespace std;

void welcome(string name, int age){
    cout << "Hello " << name << " --- Age: " << age;
}

int main() {

    string name;
    int age;
    cout << "Enter your name: ";
    getline(cin, name); // John Smith
    cout << "Enter your age: ";
    cin >> age; // 55
    welcome(name, age); // Hello John Smith --- Age: 55

    return 0;
}

// NOTE: It will not work if you put the function welcome() below the main()
// UNLESS you initialize it above the main() liek this below
#include <iostream>

using namespace std;

void welcome(string name);

int main(){
	string user = "Steve";
	welcome(user);
}

void welcome(string name){
	cout << "Welcome " << name; // Welcome Steve
}

=======
#define Funciton "Returning the value"
// void function is not returning any value

double cube(double n){
    return n * n * n;
    cout << "hello"; // <-- This line right here will not be executed because there is a return statement above
}

int main() {
    double n;
    cout << "Enter n: ";
    cin >> n; // 3
    cout << "The cube for " << n << " = " << cube(n); // The cube for 3 = 27
}

/* IF-ELSE STATEMENT
========================================*/
int main(){
	bool paid = true;

	if(paid){
		cout << "You have paid the bill."; // This will be printed if paid == true
	} else {
		cout << "Please pay as soon as possible!"; // This will be printed if paid == false
	}
}

#Boolean_Opearators "&& , || , !"
bool x = true, y = false;
if(x && y) {
	cout << "Both true";
} else if (x || y) {
	cout << "At least one is true"; // This will be printed in this case
} else {
	cout << "Both false";
}

#Boolean_Operator "=="
if(x){
	cout << "x is true";
}
// OR
if(x == true){
	cout << "x is true";
}

#Boolean_Operator "!="
if(!x){
	cout << "x is false";
}
// OR
if(x != true){
	cout << "x is false";
}

=======
#define If_Else "Comparing 3 numbers"
int getMax(int x, int y, int z){
    if(x >= y && x >= z) return x;
    else if (y >= x && y >= z) return y;
    else return z;
}

int main(){
	cout << getMax(5,5,2); // 5
}

/* SWITCH STATEMENT
========================================*/
int dayNum;
cout << "Enter a number from 0 - 6: ";
cin >> dayNum;

string day;

switch (dayNum) {
    case 0:
        day = "Sunday";
        break;
    case 1:
        day = "Monday";
        break;
    case 2:
        day = "Tuesday";
        break;
    case 3:
        day = "Wednesday";
        break;
    case 4:
        day = "Thursday";
        break;
    case 5:
        day = "Friday";
        break;
    case 6:
        day = "Saturday";
        break;
    default:
        cout << "Invalid number";
        exit(0);
        break;
}

cout << "The day is " << day;

/* WHILE LOOP
========================================*/
int countdown = 10;

while(countdown > 0){
	cout << countdown << ' ';
	coundown--; // This is a MUST to avoid INFINITY LOOPING that may crash your system [CTRL + C to break the loop]
}
cout << "- Blast off!";
// 10 9 8 7 6 5 4 3 2 1 - Blast off!

while(countdown > 0){
	cout << countdown-- << ' ';
}
cout << "- Blast off!";
// NOTE: Refer to OPERATOR's #define Arithmetic_Operators "Maths"

int x = 6;

while(x <= 5) {
	cout << x; // This will not be executed since they check x is not <= 5
}

=======
#define do_while_loop "The code block in the do block will be executed no matter what"

int x = 6;

do {
	cout << x << endl; // It will print 6 then done
	x++;
} while (x <= 5);	

=======
#define While_Loop "Guessing number"
int secretNum = 5;
int guess;
int chance = 3;
int tried = 0;
bool gameOver = false;

while(secretNum != guess && !gameOver){
    if(tried != chance) {
        cout << "Enter guess: ";
        cin >> guess;
        if(guess == secretNum) {
            cout << "You win!";
            break;
        }
        tried++;
    } else {
        gameOver = true;
        cout << "You lose!";
    }
}

// Simpler version
int secretNum = 5, guess, chance = 3;

while(chance > 0){
    cout << "Enter guess: ";
    cin >> guess;
    if(guess == secretNum) {
        cout << "You win!";
        break;
    } else {
        chance--;
        if (chance == 0) cout << "You lose!";
    }
}

/* FOR LOOP
========================================*/
#define For_Loop "Increment"
for (int i = 0; i < 10; i++){
	cout << i << " "; // 0 1 2 3 4 5 6 7 8 9 NOTE: 10 is not included as the i < 10
}

=======
#define For_Loop "Decrement"
for (int i = 10; i > 0; i--){
	cout << i << " "; // 10 9 8 7 6 5 4 3 2 1 NOTE: 0 is not included as the i > 0
}

=======
#define For_Loop "Array"
int num[] = {99, 88, 77, 66, 55};
int numLength = sizeof(num) / sizeof(num[0]);

for(int i = 0; i < numLength; i++){
	cout << num[i] << " "; // 99 88 77 66 55
}

// Simpler version
for (auto i: num){
	cout << i << " "; // 99 88 77 66 55
}

/* GETTING THE FILE SIZE
========================================*/
/* Reference
File seeker: https://www.youtube.com/watch?v=xBoMVv8uXG0
Precision: https://stackoverflow.com/questions/5907031/printing-the-correct-number-of-decimal-points-with-cout
*/
#include <iomanip>
#include <fstream>

using namespace std;

int main(){
    ifstream ifs ("test.exe", ios::binary);
    float fileSize = (float)ifs.seekg(0, ios::end).tellg()/(float)1024;
    cout << fixed << setprecision(1) << "Size of the file is "<< fileSize << " kbytes";
    return 0;
}

/* INPUT & OUTPUT WITH FILES
========================================*/
/* Reference
https://www.cplusplus.com/doc/tutorial/files/
*/

#define ofstream "Stream class to write on files"
#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ofstream writer;
	writer.open ("example.txt"); // Like opening a file
	writer << "This is the first line.\n";
	writer << "Hello ";
	writer << "World!\n";
	writer.close(); // NOTE: Must close it.
}

// NOTE: .open(filename, mode);
#define mode "an optional parameter with a combination of the following flags"
/*
ios::in		- Open for input operations.
ios::out	- Open for output operations.
ios::binary	- Open in binary mode.
ios::ate	- Set the initial position at the end of the file. If this flag is not set, the initial position is the beginning of the file.
ios::app	- All output operations are performed at the end of the file, appending the content to the current content of the file.
ios::trunc	- If the file is opened for output operations and it already existed, its previous content is deleted and replaced by the new one.
*/

// Example for writing a binary file
ofstream myFile;
myFile.open("example.bin", ios::out | ios::app | ios::binary);	

=======
#define ifstream "Stream class to read from files"


=======
#define fstream "Stream class to both read and write from/to files."
