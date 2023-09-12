#!/usr/bin/node
const { argv } = require('process');
if (argv.length === 2 || argv.length === 3) {
  console.log(0);
}
if (argv.length > 3) {
  const array = [];
  for (let i = 2; i < argv.length; i++) { array[i - 2] = parseInt(argv[i]); }
  const max = Math.max(...array);
  let second;
  second = array[0];
  for (let i = 0; i < array.length; i++) { if (array[i] > second && max > array[i]) { second = array[i]; } }
  console.log(second);
}
