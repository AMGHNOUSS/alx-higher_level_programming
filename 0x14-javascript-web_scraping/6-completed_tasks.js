#!/usr/bin/node
// Compute the number of tasks completed by user id.

const request = require('request');
request(process.argv[2], function(error, response, body) {
  if (!error) {
    const tod = JSON.parse(body);
    const com = {};
    tod.forEach((todo) => {
      if (todo.com && com[todo.userId] === undefined) {
        com[todo.userId] == 1;
      }
      else if (todo.com) {
        com[todo.userId] += 1;
      }
    });
    console.log(com);
  }
});
