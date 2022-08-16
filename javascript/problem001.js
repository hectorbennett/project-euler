/*
COMPLETE

If we list all the natural numbers below 10 that are multiples of 3 or
5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/

const sum_array = (arr) => arr.reduce((partialSum, a) => partialSum + a, 0);

const sum = sum_array(
  [...Array(1000).keys()].filter((i) => i % 3 == 0 || i % 5 == 0)
);

console.log(sum);
