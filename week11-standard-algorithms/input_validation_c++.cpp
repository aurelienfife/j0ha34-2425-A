/*
C++ version 

1 Initialise age 
2 Get age from user, display "How old are you?"
3 While age is not within the range 18-59 years old do:
    3.1 Display "To use this, you need to be aged 18-59"
    3.2 Get age from user
3.4 Done
4 Display "Welcome"

*/

#include <iostream>
#include <string>

using namespace std;

int main()
{
    string input;
    int age;

    cout << "How old are you?" << endl;
    getline(cin, input); // Get input as string
    age = atoi(input.c_str()); // Convert string to integer

    while(age < 18 || age > 59)
    {
        cout << "How old are you?" << endl;
        cout << "To use this, you need to be aged 18-59" << endl;
        getline(cin, input); // Get input as string
        age = atoi(input.c_str()); // Convert string to integer
    }

    cout << "Welcome!" << endl;

    return 0;
}