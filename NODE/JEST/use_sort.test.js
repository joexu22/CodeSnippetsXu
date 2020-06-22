const sort = require('./sort');

var numbers = [1,4,5,4,2,5,4,0];

console.log(sort(numbers))

test('expect array to be sorted', () => {
    expect(sort(numbers)).toStrictEqual([0,1,2,4,4,4,5,5]);
});
