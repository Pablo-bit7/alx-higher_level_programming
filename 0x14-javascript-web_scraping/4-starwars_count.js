#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const wedgeId = 18;

if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <API URL>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  if (response.statusCode === 200) {
    const data = JSON.parse(body).results;
    const count = data.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeId}/`)).length;
    console.log(count);
  } else {
    console.error(`Error: ${response.statusCode}`);
  }
});
