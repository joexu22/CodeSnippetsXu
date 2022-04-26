function doLongTask(task) {
    setTimeout(function () {
        console.log(`doing long ${task}`);
    }, 500);
}

function doTask(task) {
    console.log(`doing ${task}`);
}

function doThings() {
    function inOrder(firstThing, sencondThing) {
        firstThing();
        sencondThing();
    }

    function inOrderWithCallback(firstThing, callback) {
        firstThing();
        callback();
    }

    //inOrder(function(){doLongTask('1st task')}, function(){doTask('2nd task')});
    inOrderWithCallback(function(){doLongTask('1st task')}, function(){doTask('2nd task')});
}

doThings();
doLongTask('1st Task').then(doTask('2nd Task'))