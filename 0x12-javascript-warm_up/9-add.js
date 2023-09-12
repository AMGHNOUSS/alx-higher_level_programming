#!/usr/bin/node
function add (a, b) { return (a + b); }
const { argv } = require('process');
const a = parseInt(argv[2]);
const b = parseInt(argv[3]);
console.log(add(a, b));
