#!/usr/bin/node
// Read Content Of File using Request

const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
