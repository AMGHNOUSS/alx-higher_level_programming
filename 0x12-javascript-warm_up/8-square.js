#!/usr/bin/node
const { argv } = require('process');
const number = parseInt(argv[2]);
if (number) { for (let i = 0; i < number; i++) { for (let j = 0; j < number; j++) { process.stdout.write('X'); } console.log(); } } else { console.log('Missing size'); }
