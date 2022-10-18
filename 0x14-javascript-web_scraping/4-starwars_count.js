#!/usr/bin/node
const request = require('request');
int count = 0;
let url = 'https://swapi-api.hbtn.io/api/films/';
request(url, function (error, response, body) {
  if(JSON.parse(body).title == "https://swapi-api.hbtn.io/api/people/18/")
    {
      count++;	    
    }
    console.log(error || count);
});
