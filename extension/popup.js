document.getElementById("check").addEventListener("click", async () => {
  let url = document.getElementById("sms").value.trim();

  if (url === "") {
    alert("Please enter a valid sms/mail/URL.");
    return;
  }

  fetch("http://localhost:5000/url", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ url: url }),
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("response").innerText =
        "Response: " + JSON.stringify(data);
    })
    .catch((error) => console.error("Error:", error));
});
