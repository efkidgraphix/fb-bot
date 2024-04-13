const axios = require('axios');
const PAGE_ACCESS_TOKEN = 'your_page_access_token'; // You need to generate this token
const PAGE_ID = 'your_page_id'; // The ID of the Facebook page where you want to post

// Function to post a message to the Facebook page
function postLiveScore(scoreMessage) {
  const url = `https://graph.facebook.com/${PAGE_ID}/feed`;
  const data = {
    message: scoreMessage,
    access_token: 612cd116f77d5e962f8e77c279d649dd,
  };

  axios.post(url, data)
    .then(response => {
      console.log('Score posted successfully:', response.data);
    })
    .catch(error => {
      console.error('Error posting score:', error.response.data);
    });
}

// Example usage
const liveScore = 'Current match score: Team A 250/3 vs Team B';
postLiveScore(liveScore);
