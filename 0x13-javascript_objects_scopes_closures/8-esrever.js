#!/usr/bin/node
exports.esrever = function (list) {
  const counter = [];
  let i = list.length - 1;
  let j = 0;
  while (i >= 0) {
    counter[j] = list[i];
    i--;
    j++;
  }
  return (counter);
};
