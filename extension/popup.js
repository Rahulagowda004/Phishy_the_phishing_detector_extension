document.addEventListener('DOMContentLoaded', function() {
  const detectButton = document.getElementById('detectButton');
  const urlInput = document.getElementById('urlInput');
  const resultText = document.getElementById('resultText');

  detectButton.addEventListener('click', function() {
    const url = urlInput.value.trim();
    if (url) {
      detectPhishing(url);
    } else {
      resultText.textContent = 'Please enter a valid URL';
    }
  });

  async function detectPhishing(url) {
    // Replace with your phishing detection API endpoint
    const apiUrl = 'https://api.example.com/detect-phishing';
    
    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url })
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      if (data.is_phishing) {
        resultText.textContent = 'Phishing Alert: This URL is dangerous!';
      } else {
        resultText.textContent = 'No phishing detected. URL is safe.';
      }
    } catch (error) {
      console.error('Error detecting phishing:', error);
      resultText.textContent = 'Error detecting phishing. Please try again later.';
    }
  }
});
