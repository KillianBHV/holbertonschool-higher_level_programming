const request = fetch("https://swapi-hbtn.io/api/people/5/?format=json")
const result = request.json();
document.querySelector("#character").textContent = result['name'];
