/*
If we list all the natural numbers below 10 that are multiples of 3 or
5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/

#include <iostream>

using namespace std;

int main() {
    int TOTAL = 0;

    for (int X = 1; X < 1000; X += 1) {
        if (X % 3 == 0 or X % 5 == 0) {
            TOTAL += X;
        }
    }

    cout << TOTAL << endl;
}
