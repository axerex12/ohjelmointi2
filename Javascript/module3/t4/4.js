'use strict';
const div = document.querySelector("#target")
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];
for (let i =0; i< students.length; i++){
let p = document.createElement('option');
p.value = `${students[i].id}`
  p.innerHTML = `${students[i].name}`
div.appendChild(p)
}