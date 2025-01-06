// Fetch a random quote from an external API
function fetchQuote() {
  fetch('https://api.quotable.io/random')  // Using a free quote API for testing
      .then(response => response.json())
      .then(data => {
          document.getElementById('quote-text').innerText = `"${data.content}" - ${data.author}`;
      })
      .catch(error => {
          console.error('Error fetching quote:', error);
      });
}

// Load a quote when the page loads
window.onload = fetchQuote;