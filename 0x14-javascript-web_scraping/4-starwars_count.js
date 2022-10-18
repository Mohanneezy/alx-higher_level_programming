#!/usr/bin/node
const request = require('request');
int count = 0;
request(process.argv[2], function (error, response, body) {
  if(JSON.parse(body).result.characters == 'https://swapi-api.hbtn.io/api/people/18/')
    {
      count = count + 1;	    
    }
      console.log(count);
});
