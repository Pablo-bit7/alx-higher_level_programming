#!/usr/bin/node

exports.esrever = function(list) {
  let reversed = [];
  
  // Iterate through the list from end to start and push elements to reversed array
  for (let i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  
  return reversed;
};
