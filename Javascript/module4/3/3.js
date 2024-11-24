document.getElementById('searchForm').addEventListener('submit', async (event) => {
    event.preventDefault();

    const query = document.getElementById('query').value;
    const apiUrl = `https://api.tvmaze.com/search/shows?q=${query}`;

    try {
        const response = await fetch(apiUrl);
        const data = await response.json();
        displayResults(data);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
});

function displayResults(data) {
    const resultContainer = document.getElementById("result");
    resultContainer.innerHTML = ""; // Clear previous results

    data.forEach(tvShow => {
        const show = tvShow.show;


        const article = document.createElement("article");


        const title = document.createElement("h2");
        title.textContent = show.name;
        article.appendChild(title);


        const link = document.createElement("a");
        link.href = show.url;
        link.textContent = "details";
        link.target = "_blank";
        article.appendChild(link);

        if (show.image?.medium) {
            const image = document.createElement("img");
            image.src = show.image.medium;
            image.alt = show.name;
            article.appendChild(image);
        }

        const summary = document.createElement("div");
        summary.innerHTML = show.summary || "No summary available.";
        article.appendChild(summary);

        resultContainer.appendChild(article);
    });
}
