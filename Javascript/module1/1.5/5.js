vuosi = parseInt(prompt("Please enter a year:"));

if ((vuosi % 4 === 0 && vuosi % 100 !== 0) || (vuosi % 400 === 0)) {
    document.querySelector("#tulos").innerHTML = `${vuosi} on karkausvuosi`;
} else {
    document.querySelector("#tulos").innerHTML = `${vuosi} ei ole karkausvuosi`;
}