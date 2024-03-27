#!/usr/bin/node
// Print The Title of a Star Wars movie.
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  console.log(SON.parse(body).title);
});
