#!/usr/bin/node
// Print The Title of a Star Wars movie.
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url + process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title)
});
