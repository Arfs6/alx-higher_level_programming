#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
  process.exit();
}

let numArray = [...process.argv];
numArray = numArray.slice(2);
numArray.forEach((num, idx, arr) => arr[idx] = parseInt(num));
numArray.sort((a, b) => b - a);
console.log(numArray);
console.log(numArray[1]);
