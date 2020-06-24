//!!!WARNING!!! - setTimeout breaks things - !!!WARNING!!!
//Something is going on that makes it so that it doesn't really work the way I think it works

function doTask(task, callback) {
    console.log(`doing ${task}`);
    callback();
}

function doLongTask(task, callback) {
    setTimeout(function () {
        console.log(`doing long ${task}`);
    }, 500);
    callback();
}

function doLastTask () {};

doLongTask('1st task', function () {doTask('2nd task', doLastTask)});