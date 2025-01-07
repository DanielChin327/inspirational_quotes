// Fetch a quote from your Flask backend instead of the external API directly
function fetchQuote() {
  fetch("http://127.0.0.1:5000/api/quote")
      .then(response => response.json())
      .then(data => {
          // Assuming the data structure returned matches your API response
          document.getElementById('quote-text').innerText = `"${data[0].q}" - ${data[0].a}`;
      })
      .catch(error => console.error('Error fetching quote:', error));
}

// Load a quote when the page loads
window.onload = fetchQuote;