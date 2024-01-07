#!/usr/bin/node

const request = require('request');
const { argv } = require('process');
const BaseUrl = 'https://swapi-api.alx-tools.com/api/films/';

request(BaseUrl + argv[1], (error, response, body) => {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
