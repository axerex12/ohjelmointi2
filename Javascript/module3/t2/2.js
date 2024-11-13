const div = document.querySelector("#target")
const p = document.createElement('li');
const html = "<li>First item</li>\n" +
    "<li>Second item</li>\n" +
    "<li>Third item</li>";
p.innerHTML = html
div.appendChild(p)

const second = document.getElementsByTagName('li')[2];
second.classList.add("my-item")