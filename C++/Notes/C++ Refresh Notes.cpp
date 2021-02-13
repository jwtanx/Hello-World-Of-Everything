/* BASICS OF C++
========================================
Last updated: Sat, February 13, 2021 - 21:40
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
// Normal printing
cout << "1";
cout << "2";
cout << "3";
// Output: 123

// With 'endl;' behind
cout << "1" << endl;
cout << "2" << endl;
cout << "3" << endl;
/* Output:  1
            2
            3
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