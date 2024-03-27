#!/usr/bin/node
// Write content of web page to a File.
const fs = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
