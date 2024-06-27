class URLFetcher {
  constructor() {
    this.el = document.getElementById("site_score");
    this.el2 = document.getElementById("site_msg");
  }

  fetchURL() {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      var tab = tabs[0];
      var url = tab.url;
      // Optionally alert the URL
      // alert(url);

      fetch("http://localhost:5000/post", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: `URL=${encodeURIComponent(url)}`,
      })
        .then((response) => response.text())
        .then((data) => this.handleResponse(data))
        .catch((error) => console.error("Fetch error:", error));
    });
  }

  handleResponse(data) {
    console.log("Server response:", data);
    if (parseInt(data) == 1) {
      this.displayWarning();
    } else if (parseInt(data) == 0) {
      this.displaySafe();
    }
  }

  displayWarning() {
    alert("Phishing");
    console.log("1");
    this.el.textContent = "Phishing";
    this.el2.textContent = "This website may not be safe >_<";
    this.el.style.background = "linear-gradient(45deg, #a64812, #e1e354);";
    this.el.style.transform = "translateZ(25px)";
  }

  displaySafe() {
    console.log("0");
    this.el.textContent = "Safe";
    this.el2.textContent = "This website is safe to use UwU";
    this.el.style.background = "linear-gradient(45deg, #00db2f, #06678b)";
    this.el.style.transform = "translateZ(25px)";
  }
}
