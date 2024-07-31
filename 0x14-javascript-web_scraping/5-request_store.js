#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Usage: ./5-request_store.js <URL> <file path>');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  fs.writeFile(filePath, body, 'utf8', err => {
    if (err) {
      console.error('Error:', err);
      process.exit(1);
    }
  });
});
