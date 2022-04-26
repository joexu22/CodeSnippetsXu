/* This compares 3 command line arguments and see if they are all equal */

// console.log(process.argv);
// console.log(process.argv[2])
// console.log(process.argv[3])
// console.log(process.argv[4])

let bool1 = process.argv[2] === process.argv[3];
let bool2 = process.argv[2] === process.argv[4];
let bool3 = process.argv[3] === process.argv[4];

bool_out = bool1 && bool2 && bool3;

console.log(bool_out);