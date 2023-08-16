#!/usr/bin/node
const data = require('./101-data');
const sortedData = {};
for (entry of Object.entries(data.dict)) {
  if (typeof sortedData[entry[1]] === 'undefined') {
    sortedData[entry[1]] = [];
  }
  sortedData[entry[1]].push(entry[0]);
}
console.log(sortedData);
