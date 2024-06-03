#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function requestCharacter (characterList, index) {
  if (characterList.length === index) {
    return;
  }

  request(characterList[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      requestCharacter(characterList, index + 1);
    }
  });
}

request(movieUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characterList = JSON.parse(body).characters;

    requestCharacter(characterList, 0);
  }
});
