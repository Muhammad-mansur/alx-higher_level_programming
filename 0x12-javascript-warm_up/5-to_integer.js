#!/usr/bin/node

const arg = process.argv[2];
const intValue = +arg;

if (intValue) {
  console.log('My number: ' + intValue);
} else {
  console.log('Not a number');
}
