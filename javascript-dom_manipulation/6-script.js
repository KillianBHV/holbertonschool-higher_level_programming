const t = document.querySelector();
const result = fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
.then(response => response.json())
.then(response => document.querySelector("#character").textContent = response["name"]);
