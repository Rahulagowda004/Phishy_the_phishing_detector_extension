document.addEventListener("DOMContentLoaded", () => {
  const fileUrl = "output.txt"; // Replace with the path to your .txt file

  fetch(fileUrl)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.text();
    })
    .then((data) => {
      // Display the fetched contents in the HTML
      const fileContentsDiv = document.getElementById("fileContents");
      fileContentsDiv.textContent = data;
    })
    .catch((error) => {
      console.error("Error fetching the file:", error);
    });
});
