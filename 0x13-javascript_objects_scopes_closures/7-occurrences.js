#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  let size = 0;
  while (size < list.length) {
    if (list[size] === searchElement) {
      counter++;
    }
    size++;
  }
  return (counter);
};
