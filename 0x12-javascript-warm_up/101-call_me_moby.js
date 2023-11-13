#!/usr/bin/node
exports.callMeMoby = function(number, doing){
  let i = 0;
  while (i < number) {
    doing();
    i++;
  }
}
