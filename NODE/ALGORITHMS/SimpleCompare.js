var assert = require('assert');

var testNumber = function (x) {
	if ((0 < x) && (x < 1)) {
		return true;
	} else {
		return false;
	}
}

var testTwoNumbers = function (x, y) {
	return testNumber(x) && testNumber(y);
}

// console.log(testTwoNumbers(.5, .7));
assert(testNumber(0) === false);
assert(testNumber(1) === false);
assert(testTwoNumbers(.5, .7) === true);
assert(testTwoNumbers(1.5, .7) === false);
