#!/usr/bin/node

/**
 * Function to compute the factorial of a number recursively.
 * @param {number} n - The number to compute the factorial for.
 * @returns {number} - The factorial of the number.
 */
function factorial(n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }

  // Recursive case: factorial of n is n times factorial of (n-1)
  return n * factorial(n - 1);
}

const num = parseInt(process.argv[2]);

console.log(factorial(num));

