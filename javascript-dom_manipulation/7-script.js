const request = fetch('https://swapi-api.hbtn.io/api/films/?format=json');
const result = request.json();

result['results'].forEach(e => document.querySelector('#list_movies').appendChild(e));
