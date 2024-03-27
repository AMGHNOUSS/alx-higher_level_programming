#!/usr/bin/node
// Display the status code of a `GET` request.
const request = require('request');
request.get(argv[2]).on('response', function(response) {
  console.log('code :  ${response.statusCode}');
});