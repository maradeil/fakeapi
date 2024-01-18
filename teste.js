fetch('https://my-json-server.typicode.com/maradeil/fakeapi/posts', {
  method: 'POST',
  body: JSON.stringify({
    title: 'if you',
    body: 'bar',
    userId: 70,
  }),
  headers: {
    'Content-type': 'application/json; charset=UTF-8',
  },
})
  .then((response) => response.json())
  .then((json) => console.log(json));
