chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.status === "complete" && tab.active) {
    if (tab.url && !tab.url.startsWith("chrome://")) {
      // Filter out internal Chrome pages
      fetch("http://localhost:5000/url", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ url: tab.url }),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json();
        })
        .then((data) => {
          console.log("Response:", data);
          if (data.result_url === "site is not secure") {
            // Redirect to warning page
            chrome.tabs.update(tabId, { url: "warning.html" });
          } else {
            // Continue with the redirection or normal operation
          }
        })
        .catch((error) => {
          console.error("Error:", error);
          // Handle errors if needed
        });
    }
  }
});
