document.getElementById('searchForm').addEventListener('submit', async (event) => {
    event.preventDefault();

    const query = document.getElementById('query').value;
    const apiUrl = `https://api.tvmaze.com/search/shows?q=${query}`;

        const response = await fetch(apiUrl);
        const data = await response.json();
        console.log(data[0]);


});