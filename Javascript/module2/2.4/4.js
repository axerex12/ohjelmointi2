var numerot = []
for(var i = 1; i === 1;){
    var numero = parseInt(prompt("Anna numero!"))
    if (numero === 0) {
        i = 0
        break
    }
    else {
        numerot.push(numero)
    }

}
numerot.sort(function (a, b) {return b-a})

console.log(numerot)