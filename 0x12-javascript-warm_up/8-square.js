#!/usr/bin/node
const size = process.argv[2];
if (isNaN(size)) {
  console.log('Missing size');
  process.exit();
}

let i;
for (i = 0; i < size; ++i) {
  console.log('X'.repeat(size));
}
