#!/usr/bin/node
const Square = require('./5-square');

module.exports = class extends Square {
  charPrint (c) {
    let char = c;
    if (typeof c === 'undefined') {
      char = 'X';
    }

    let i;
    for (i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
};
