var numerot = []

for (i = 0; i === 0;) {
    var numero = parseInt(prompt("Anna numero"))
    if (numerot.includes(numero)){
        console.log("the number has already been given")
        i = 1
    }
    else {
        numerot.push(numero)
    }
}

numerot.sort(function (a, b) {return b-a})
for (b = 0; b < numerot.length; b+++1){
    console.log(numerot[b])
}