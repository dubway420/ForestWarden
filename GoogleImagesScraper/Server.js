const CONFIG = require('./config.json');
const fs = require('fs');
const path = require('path');
const axios = require('axios');
const GoogleImages = require('google-images');

let imageLinksFound = [];
let imagesComplete = 0;

function sleep(seconds) {
  return new Promise(resolve => setTimeout(resolve, seconds * 1000));
}

// Function to download the image from the URL and save it locally
async function downloadImage(url) {
    try {
      const response = await axios.get(url, { responseType: 'arraybuffer' });
  
      const contentType = response.headers['content-type'];
      const extension = contentType.split('/')[1];
      const filename = `image_${Date.now()}.${extension}`;
  
      const filePath = path.join(__dirname, 'files', filename);
  
      fs.writeFileSync(filePath, response.data);
  
      console.log('Image downloaded and saved:', filePath);
    } catch (error) {
      console.error('Error downloading the image:', error.message);
    }
  }

(async function Main() {

  const client = new GoogleImages(CONFIG.cse, CONFIG.apiKey);
  try {
    for(let y = 0; y < CONFIG.searchPhrases.length; y++){
        let phrase = CONFIG.searchPhrases[y];
        for(let x = 0; x < CONFIG.pages; x++){
            const images = await client.search(phrase, { page: x, size: 'large', type: 'photo' });
            for (const image of images) {
                downloadImage(image.url)
            }
            sleep(1);
        }
    }
  } catch (error) {
    console.error('Error scraping images from Google:', error);
  }

})();
