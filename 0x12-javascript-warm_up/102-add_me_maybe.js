#!/usr/bin/node

/**
 * Increments the given number by 1 and calls the specified function with the result.
 * @param {number} number - The number to be incremented.
 * @param {Function} theFunction - The function to be called.
 */
exports.addMeMaybe = function (number, theFunction) {
  // Increment the given number by 1 and call the specified function with the result
  theFunction(++number);
};

