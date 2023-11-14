#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super();
    super.width = size;
    super.height = size;
  }
}
module.exports = Square;
