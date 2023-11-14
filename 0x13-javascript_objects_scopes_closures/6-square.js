#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super();
    super.width = size;
    super.height = size;
  }

  charPrint (c) {
    if (c !== undefined) {
      this.use = 'c';
    } else {
      this.use = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(this.use);
      }
      console.log();
    }
  }
}
module.exports = Square;
