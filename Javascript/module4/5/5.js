const apiurl = "https://api.chucknorris.io/jokes/random"

async function fetchJoke() {
    const response = await fetch(apiurl);


    const data = await response.json()
    const joke = data.value

    const resultContainer = document.getElementById("result");

    resultContainer.innerHTML = ""

    const jokeElement = document.createElement("p")
    jokeElement.textContent = joke

    resultContainer.appendChild(jokeElement)

}
fetchJoke();