#!/usr/bin/node
// Print The Title of a Star Wars movie.
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url + process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  console.log(SON.parse(body).title);
});
