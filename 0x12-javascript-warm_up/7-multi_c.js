#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing numer of occurencies');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
