document.getElementById("check").addEventListener("click", async () => {
  let user_input = document.getElementById("sms").value.trim();

  if (user_input === "") {
    alert("Please enter a valid sms/mail/URL.");
    return;
  }

  fetch("http://localhost:5000/user_input", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ user_input: user_input }),
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("response").innerText =
        "Response: " + JSON.stringify(data);
    })
    .catch((error) => console.error("Error:", error));
});
