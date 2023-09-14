#!/usr/bin/node
const dict = require('./101-data.js').dict;
const dictN = {};
for (const key in dict) {
  if (dictN[dict[key]] === undefined) {
    dictN[dict[key]] = [key];
  } else {
    dictN[dict[key]].push(key);
  }
}
console.log(dictN);
