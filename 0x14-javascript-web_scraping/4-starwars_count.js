#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Please provide the API URL as the first argument.');
  process.exit(1);
}

const characterId = 18; // Wedge Antilles character ID

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to retrieve data. Status code:', response.statusCode);
  } else {
    const filmsData = JSON.parse(body);

    // Filter films where Wedge Antilles is present
    const filmsWithWedge = filmsData.results.filter(film =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );

    console.log(filmsWithWedge.length);
  }
});
