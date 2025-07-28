const t = document.querySelector("#list_movies");
const result = fetch("https://swapi-api.hbtn.io/api/films/?format=json");
.then(response => response.json())
.then(response => {
	response['results'].forEach(e => {
		li = document.createElement("li");
		li.textContent = e["title"];
		t.appendChild(li);
	}
)});
