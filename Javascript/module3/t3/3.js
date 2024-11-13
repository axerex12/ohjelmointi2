'use strict';
const div = document.querySelector("#target")
const names = ['John', 'Paul', 'Jones'];
const p = document.createElement('li');

for (let name of names){
  p.innerHTML += `<li>${name}</li>`

  div.appendChild(p)
}
