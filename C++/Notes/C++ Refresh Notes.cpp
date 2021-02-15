/* BASICS OF C++
========================================
Last updated: Sat, February 13, 2021 - 23:13

NOTE: This file is not compilable, I use the #define to highlight the syntax while writing the notes
*/

/* Hello World
========================================*/
#include <iostream>

using namespace std;

int main() {
    cout << "Hello World" << endl;
    return 0;
}

/* Printing
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

/* Variables & Data types
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

/* Operators
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

#define Assignment_Operators "Direct Assigning"
/*
x = 1   : x = 1
x += 2  : x = x + 2
x -= 3  : x = x - 3
x *= 4  : x = x * 4
x /= 5  : x = x / 5
x %= 6  : x = x % 6
*/

/* Library
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

/* Getting user input
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

/* Getting the file size
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

/* Input & Output with files
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
