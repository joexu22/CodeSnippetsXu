function doSomethingFirst(firstThing, callback) {
    console.log(`doing ${firstThing}`);
    callback();
}


function doSomethingFirstForReallyLong(firstThing, callback) {
    setTimeout(function () { console.log(`doing ${firstThing}`)}, 500);
    callback();
}

function doSomethingSecond(secondThing, callback) {
    console.log(`doing ${secondThing}`);
    callback();
}

function doSomethingThird(thirdThing, callback) {
    console.log(`doing ${thirdThing}`);
    callback();
}

function doLastThing() {
}

// 1 Thing Chain
// doSomethingFirst('first thing', doLastThing);

doSomethingFirstForReallyLong('long thing', doLastThing);

// 2 Thing Chain
doSomethingFirst('first thing', function () {
    doSomethingSecond('second thing', doLastThing)}
);

doSomethingFirst('1st thing', function() {
    doSomethingSecond('2nd thing', function() {
        doSomethingThird('3rd thing', function() {
            doLastThing;
        });
    });
});

