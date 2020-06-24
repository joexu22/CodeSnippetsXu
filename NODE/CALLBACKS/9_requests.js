const request = require('request');

URL_STRING = 'https://svgxmep77l.execute-api.us-east-1.amazonaws.com/oak/test-lambda-function-gxu';

function handleResponse(error, response, body) {
    if (error) {
        //Handle Error
        console.log(error);
    } else {
        //Success
        console.log(body);
    }
}

request(URL_STRING, handleResponse);
