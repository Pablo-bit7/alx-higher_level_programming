#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (!movieId) {
  console.error('Usage: ./100-starwars_characters.js <Movie ID>');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const characterUrls = data.characters;

    characterUrls.forEach(characterUrl => {
      request(characterUrl, (err, res, characterBody) => {
        if (err) {
          console.error('Error:', err);
          return;
        }
        if (res.statusCode === 200) {
          const characterData = JSON.parse(characterBody);
          console.log(characterData.name);
        }
      });
    });
  } else {
    console.error(`Error: ${response.statusCode}`);
  }
});
