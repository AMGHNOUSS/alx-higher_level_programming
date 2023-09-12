#!/usr/bin/node
exports.callMeMoby = function (a, fun) {
  for (let i = 0; i < a; i++) {
    fun();
  }
};
