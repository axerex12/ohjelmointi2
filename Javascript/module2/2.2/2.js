const num = parseInt(prompt("Montako osallistujaa!"))
const osallistujat = []
for (let i = 0; i < num; i++) {
        var nimi = prompt("anna nimi")
        osallistujat[i] = nimi
}
osallistujat.sort()
document.querySelector("#lista").innerHTML = osallistujat.map(nimi => `<li>${nimi}</li>`).join("");