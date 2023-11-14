#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w < 1 || w === undefined) || (h < 1 || h === undefined)) {
      return;
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
