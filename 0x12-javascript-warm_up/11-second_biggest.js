#!/usr/bin/node
function second_biggest () {
  const { argv } = require('process');
  if (argv.length === 2 || argv.length === 3) {
    return (0);
  }
  if (argv.length > 3) {
    const array = [];
    for (let i = 2; i < argv.length; i++) { array[i - 2] = parseInt(argv[i]); }
    const max = Math.max(...array);
    let second;
    second = array[0];
    for (let i = 0; i < array.length; i++) { if (array[i] > second && max > array[i]) { second = array[i]; } }
    return (second);
  }
}
if (second_biggest()) { console.log(second_biggest()); } else { console.log(0); }
