#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const numberOne = Number(process.argv[2]);
const numberTwo = Number(process.argv[3]);

console.log(add(numberOne, numberTwo));
