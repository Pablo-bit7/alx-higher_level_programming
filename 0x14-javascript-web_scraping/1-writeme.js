#!/usr/bin/node

const { argv } = process;
const fs = require('fs');

if ((process.argv.length < 4) {
  console.error('Usage: ./1-writeme.js <file path> <string to write>');
  process.exit(1);
}

fs.writeFile(argv[2], argv[3], err => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
});
