#!/usr/bin/node
const number = parseInt(process.argv[2]);
let counter = 0;
const sent = 'C is fun';
if (!isNaN(number)) {
  while (counter < number) {
    console.log(sent);
    counter++;
  }
} else {
  console.log('Missing number of occurrences');
}
