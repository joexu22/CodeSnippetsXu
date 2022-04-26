//adding callback
function doSomethingWithCallback(task, callback) {
    console.log(`doing ${task}.`);
    callback();
}

function alertAfterDoingSomething() {
    console.log('finished!')
}

doSomethingWithCallback('coding', alertAfterDoingSomething);