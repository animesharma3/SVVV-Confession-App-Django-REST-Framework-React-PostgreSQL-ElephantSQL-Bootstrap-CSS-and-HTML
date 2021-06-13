let url = 'https://letsconfess.herokuapp.com/api/confessions/create/'

data = {
    user: 1,
    title: "dsjfjsdljf",
    text: "dkfoka;lf"
}

fetch(url, {
    method: 'POST',
    headers: {
        'Content-type': 'application/json',
    },
    body: JSON.stringify(data)
})
.then(res => res.json())
.then(data => console.log(data))