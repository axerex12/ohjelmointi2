var koirat = []
for (let i = 0; i < 6; i++){
    var koira = prompt("Anna koiran nimi")
    koirat.push(koira)
}
koirat.sort()
koirat.reverse()

document.querySelector("#koirat").innerHTML = "<ul><li>" + koirat.join("</li><li>") + "</li></ul>"