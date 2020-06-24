function some30msFunction(task, callback) {
    setTimeout(function () {console.log(`doing ${task}`)}, 30);
    callback();
}

function some50msFunction(task, callback) {
    setTimeout(function () {console.log(`doing ${task}`)}, 50);
    callback();
}

function some80msFunction(task, callback) {
    setTimeout(function () {console.log(`doing ${task}`)}, 80);
    callback();
}

function intuitiveOrder() {
    some30msFunction('1st task', function () {
        some50msFunction('2nd task', function() {
            some80msFunction('3rd task', function() {
            })
        })
    })
}

function nonIntuitiveOrder() {
    some80msFunction('1st task', function () {
        some50msFunction('2nd task', function() {
            some30msFunction('3rd task', function() {
            })
        })
    })
}

//intuitiveOrder();
nonIntuitiveOrder();