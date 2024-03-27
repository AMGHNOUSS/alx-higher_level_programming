#!/usr/bin/node
// Print The Number of a Star Wars movie.
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1 
        : count;
    }, 0));
  }
});
