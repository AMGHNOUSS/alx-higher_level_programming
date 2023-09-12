#!/usr/bin/node
function factorial (n) {
  if (n < 2) { return (1); } else { return (n * factorial(n - 1)); }
}
const { argv } = require('process');
const a = parseInt(argv[2]);
if (a) { console.log(factorial(a)); } else { console.log('1'); }
