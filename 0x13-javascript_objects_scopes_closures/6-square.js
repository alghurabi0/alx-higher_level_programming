#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let line = '';
    let m, n;
    for (n = 0; n < this.width; n++) {
      line += c;
    }
    for (m = 0; m < this.width; m++) {
      console.log(line);
    }
  }
}

module.exports = Square;
