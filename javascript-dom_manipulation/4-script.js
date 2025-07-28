const i = document.querySelector("#add_item");
ul = document.createElement('ul');
ul.classList.add('add_item');
li = document.createElement('li');
li.textContent = 'Item';

i.appendChild(ul).appendChild(li);
