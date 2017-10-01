/*
Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
*/

#include <iostream>

using namespace std;

int fib_sum( int limit ) {
    int alpha = 1;
    int beta = 1;
    int fib = 1; 
    
    int total = 0;

    while ( fib < limit ) {
        if ( fib % 2 == 0 ) {
            total += fib;
        }
        fib = alpha + beta;
        alpha = beta;
        beta = fib;
    }

    return total;
}

int main()
{
    cout << fib_sum( 4000000 ) << endl;
    return 0;
}