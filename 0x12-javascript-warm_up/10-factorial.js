#!/usr/bin/node
function factorise (a) {
  if (a > 0) {
    return (a * factorise(a - 1));
  } else {
    return 1;
  }
}
const number = parseInt(process.argv[2]);
console.log(factorise(number));
