#!/usr/bin/node
exports.esrever = function (list) {
  const revList = [];
  let i;
  for (i = 0; i < list.length; i++) {
    revList.push(list[list.length - (i + 1)]);
  }
  return revList;
};
