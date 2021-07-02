var assert = require('assert');

function fibonacci(size) {
	var first = 0;
	var second = 1;
	var next;
	count = 2;
	result = [first, second];

	if (size < 2) {
		return "the request was made but it was not good"
	}

	while (count++ < size) {
		next = first + second;
		first = second;
		second = next;
		result.push(next);
	}

	return result;
}

//console.log(fibonacci(10));
let fib10 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34];
//assert(fibonacci(10) === fib10); // This does not work; need special array compare

// JSON Method
assert(JSON.stringify(fibonacci(10)) === JSON.stringify(fib10));

// toSting() Method
assert(fibonacci(10).toString() === fib10.toString());

// Array.prototype.every() Method
assert(fibonacci(10).length === fib10.length && fibonacci(10).every((value, index) => value === fib10[index]));