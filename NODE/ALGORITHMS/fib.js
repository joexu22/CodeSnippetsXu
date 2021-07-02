var fib = function (n) {
	let first = 0;
	let second = 1;
	let next;
	let count = 2;
	let result = [first, second];

	if (n < 2) {
		return "not valid n";
	}
	while (count++ < n) {
		next = first + second;
		first = second;
		second = next;
		result.push(next);
	}
	return result;
}

console.log(fib(10));