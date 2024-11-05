function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

rand = getRandomInt(4)
user = prompt("Anna nimesi")

if (rand === 0) {
    talo = "Gryffindor"

}else if (rand === 1) {
    talo = "Slytherin"
}else if (rand === 2) {
    talo = "Hufflepuff"
}else {
    talo = "Ravenclaw"
}

talojanimi = `${user} sinä olet ${talo}!`

document.querySelector("#talojanimi").innerHTML = talojanimi;