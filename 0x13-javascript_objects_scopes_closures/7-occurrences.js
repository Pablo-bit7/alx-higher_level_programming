#!/usr/bin/node

exports.nbOccurences = function(list, searchElement) {
  let count = 0;
  
  // Iterate through the list and count occurrences of searchElement
  for (let element of list) {
    if (element === searchElement) {
      count++;
    }
  }
  
  return count;
};
