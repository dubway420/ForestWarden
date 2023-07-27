from serpapi import GoogleSearch
from keys import api_key
import requests
import os

# Search term ---------------------------------------------
# search_term = "forest fire"

class GoogleImageScrapper:

    def __init__(self, search_term, increment=None):

        """
        Make any set-up initialisations which need to be completed, such as creating folders
        for scraped images. 

        Arguments:

        search_term: a term to be google image searched and the images retrieved 
        
        """

        self.search_term = search_term

        # Generate a folder path for saving scraped images too
        search_term_no_spaces = search_term.replace(" ", "_")
        data_folder = os.path.join("image_data", search_term_no_spaces)

        number_existing_files = 0

        # If the folder doesn't already exist, create it
        if not os.path.exists(data_folder):
            os.mkdir(data_folder)

        # If the folder does exist, count the number of files inside to use for file naming purposes    
        else:
            number_existing_files = len(os.listdir(data_folder))

        
        self.data_folder = data_folder
        self.number_existing_files = number_existing_files


        if increment:
            self.increment = increment
        else:
            # The search API finds images in batches of 100. This finds the increment number of previous searches
            self.increment = str(int(number_existing_files / 100))

        self.api_call_done = False
        

    def api_call(self):

        params = {
        "q": self.search_term,
        "engine": "google_images",
        "ijn": self.increment,
        "api_key": api_key
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        self.api_results = results["images_results"]

        self.api_call_done = True


    def save_images(self):

        if not self.api_call_done:
            print("Warning: call the method api_call() before running this method")
            return

        for i, result in enumerate(self.api_results):
            image_url = result['original']

            try:
                img_data = requests.get(image_url, timeout=20).content

            except:
                print("Image retrieval operation failed on", image_url)

            image_name = "image" + str(i + self.number_existing_files) + ".jpg"
            image_path = os.path.join(self.data_folder, image_name)

            with open(image_path, 'wb') as handler:
                handler.write(img_data)