async function predict() {
  const response = await fetch("http://localhost:8000/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      value: 10
    })
  });

  const result = await response.json();

  console.log(result.prediction);
}
