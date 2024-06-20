#!/usr/bin/node
const fs = require('fs');
const path = require('path');

// Ensure we have the correct number of arguments
if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

// Read the content of fileA
fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) {
    console.error(`Error reading ${fileA}: ${err.message}`);
    process.exit(1);
  }

  // Read the content of fileB
  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) {
      console.error(`Error reading ${fileB}: ${err.message}`);
      process.exit(1);
    }

    // Concatenate dataA and dataB
    const concatenatedData = dataA.trim() + '\n' + dataB.trim();

    // Write the concatenated data to fileC
    fs.writeFile(fileC, concatenatedData, err => {
      if (err) {
        console.error(`Error writing to ${fileC}: ${err.message}`);
        process.exit(1);
      }
      console.log(`Concatenation successful. Output written to ${fileC}`);
      console.log();
    });
  });
});
