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
text.substr(8, 5) // A sen

#String Replacing
// str.replace(STARTING_INDEX, NUMBER_OF_CHAR_BEHIND_TO_REPLACE, REPLACE_WITH);
text.replace(10, -1, "replacement"); // This is A replacement
text.replace(10, 0, "new "); // This is A new sentence
text.replace(10, 3, "new"); // This is A newtence

##CONTINUE - https://youtu.be/vLnPwxZdW4Y?t=2863

=======
#define Integer "Assigning"
int age = 22;

#define Float "Used on specific occasion"
float price = 12.99

=======
#define Double "Can store more decimal point than float"
double pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286

=======
#define Character
char grade = 'F' // Make sure it is single quote

=======
#define Boolean
bool paid = true;
bool ate = false;

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