const num1 = parseInt(prompt("Anna numero!"));
const num2 = parseInt(prompt("Anna numero!"));
const num3 = parseInt(prompt("Anna numero!"));
const num4 = parseInt(prompt("Anna numero!"));
const num5 = parseInt(prompt("Anna numero!"));

const taulukko = [num1, num2, num3, num4, num5]

for (let i = taulukko.length-1; i >= 0; i--) {
    console.log(`Numero: ${taulukko[i]}`);
}