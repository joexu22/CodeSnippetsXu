let myFirstPromise = new Promise(function(resolve, reject) {
    setTimeout(function () {resolve("Success!")}, 250)
})

myFirstPromise.then(function(successMessage) {
    console.log("Yay! " + successMessage)
});