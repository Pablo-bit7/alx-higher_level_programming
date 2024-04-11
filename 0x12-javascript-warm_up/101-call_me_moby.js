#!/usr/bin/node

/**
 * Calls the specified function `x` times.
 * @param {number} x - The number of times to call the function.
 * @param {Function} theFunction - The function to be called.
 */
exports.callMeMoby = function (x, theFunction) {
  // Iterate `x` times and call the specified function
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};

