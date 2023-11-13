#!/usr/bin/node
let first = 0;
let second = 0;
let check = 0;
let temp;
let counter = 2;
while (counter < process.argv.length)
{
  if (check > first) {
    temp = first;
    first = second;
    second = temp;
  }
  check = parseInt(process.argv[counter]);
  if (check > second){
     second = check;
  }
  counter++;
}
console.log(second);
