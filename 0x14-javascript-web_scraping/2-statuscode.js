#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

if (!url) {
  console.error('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  console.log('code:', response.statusCode);
});
