// async function predict() {
//   const response = await fetch("http://localhost:8000/predict", {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json"
//     },
//     body: JSON.stringify({
//       value: 10
//     })
//   });

//   const result = await response.json();

//   console.log(result.prediction);
// }
async function predict() {

    const response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            size: Number(document.getElementById("size").value),
            bedrooms: Number(document.getElementById("bedrooms").value),
            distance: Number(document.getElementById("distance").value)
        })
    });


    const data = await response.json();

    document.getElementById("result").innerHTML =
        `Price: £${data.prediction.toFixed(2)}`;
}