#!/usr/bin/node
const number = parseInt(process.argv[2]);
let counter = 0;
let i = 0;
const sent = 'X';
if (!isNaN(number)) {
  while (counter < number) {
    while (i < number) {
      process.stdout.write(sent);
      i++;
    }
    console.log();
    i = 0;
    counter++;
  }
} else {
  console.log('Missing size');
}
