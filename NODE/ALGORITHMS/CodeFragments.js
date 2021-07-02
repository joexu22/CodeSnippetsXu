let t = 9;
while (Math.abs(t - 9.0/t) > .001) {
	t = (9.0/t + t) / 2.0;
	console.log(t);
}

let sum = 0;
for (var i = 1; i <= 1000; i++) {
	for (var j = 0; j < i; j++) {
		sum++;
	}
}
console.log(sum)

let val = 0;
for (var i = 1; i <= 1000; i *= 2) {
	for (var j = 0; j < 1000; j++) {
		val++;
	}
}
console.log(val)