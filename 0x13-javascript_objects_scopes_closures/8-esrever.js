#!/usr/bin/node
exports.esrever = function (list) {
  const listR = [];
  for (let i = list.length - 1; i >= 0; i--) {
    listR[list.length - i - 1] = list[i];
  }
  return (listR);
};
