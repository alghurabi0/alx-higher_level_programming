#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w < 1 || h < 1) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let h, w;
    let line = '';
    for (w = 0; w < this.width; w++) {
      line += 'X';
    }
    for (h = 0; h < this.height; h++) {
      console.log(line);
    }
  }
}

module.exports = Rectangle;
