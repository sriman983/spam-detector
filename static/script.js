function checkSpam() {
    let emailText = document.getElementById("emailText").value;

    fetch('/predict', {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: "email_text=" + encodeURIComponent(emailText)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("prediction").innerText = data.prediction;
        document.getElementById("score").innerText = data.score;
        document.getElementById("probability").innerText = (data.probability * 100).toFixed(2) + "%";
    });
}