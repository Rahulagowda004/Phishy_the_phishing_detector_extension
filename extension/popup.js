document
  .getElementById("fetchUrlButton")
  .addEventListener("click", async () => {
    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    let url = tab.url;

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
