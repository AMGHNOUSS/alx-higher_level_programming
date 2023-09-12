#!/usr/bin/node
const SquareOld = require('./5-square.js');
class Square extends SquareOld {
  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.height; j++) {
        process.stdout.write(c);
      }
      console.log();
    }
  }
}
module.exports = Square;
