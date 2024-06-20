#!/usr/bin/node
const { dict } = require('./101-data');

// Initialize an empty object to store result
const sortedDict = {};

// Iterate through keys of original dict
Object.keys(dict).forEach(userId => {
  const occurrences = dict[userId];
  
  // If the occurrences value is not yet a key in sortedDict, initialize it as an empty array
  if (!(occurrences in sortedDict)) {
    sortedDict[occurrences] = [];
  }
  
  // Push the userId to the array corresponding to its occurrences value
  sortedDict[occurrences].push(userId);
});

console.log(sortedDict);
