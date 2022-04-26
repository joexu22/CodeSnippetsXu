const assert = require('assert');

var gcd = function(a, b) {
    if (b === 0) {
        return a;
    }
    var c = a % b;
    return gcd(b, c);
}

assert.strictEqual(gcd(21, 12), 3)
assert.strictEqual(gcd(12, 21), 3)
console.log(gcd(21, 12));
console.log(gcd(12, 21));
console.log(12 % 21);