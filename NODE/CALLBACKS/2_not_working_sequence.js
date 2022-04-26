function first() {
    setTimeout(function () {
        console.log(1);
    }, 500);
}

function second() {
    console.log(2);
}

function third() {
    console.log(3);
}

first();
second();
third();