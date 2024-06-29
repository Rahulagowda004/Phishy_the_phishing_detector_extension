document.addEventListener("DOMContentLoaded", function () {
  // Fetch current tab URL immediately on popup load
  fetchCurrentTabUrl();

  // Add event listener to send button
  const sendButton = document.getElementById("send-button");
  sendButton.addEventListener("click", function () {
    const userInput = document.getElementById("user-input").value;
    sendInputToServer(userInput);
  });
});

function fetchCurrentTabUrl() {
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    let currentTab = tabs[0];
    let currentUrl = currentTab.url;

    // Display the URL in the popup
    document.getElementById("url").textContent = currentUrl;
  });
}

function sendInputToServer(input) {
  // Store input in a variable called inputUser
  let inputUser = input;
  console.log("Input from user:", inputUser);

  // Send input to the backend server
  fetch("http://localhost:3000/save-input", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ input: inputUser }),
  })
    .then((response) => response.text())
    .then((data) => {
      console.log("Response from server:", data);
    })
    .catch((error) => {
      console.error("Error sending input to server:", error);
    });
}
