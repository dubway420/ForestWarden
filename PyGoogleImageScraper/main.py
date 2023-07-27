from scraper import GoogleImageScrapper

search_term = "forest fire from above"
iterations = 2
starting_increment = None

scraper = GoogleImageScrapper(search_term, increment=starting_increment)

for i in range(iterations):

    print("\n==============\n")
    print(f"\nIncrement: {scraper.increment}")
    print(f"Images scrapped for category {search_term}: {scraper.number_existing_files}")

    scraper.api_call()
    scraper.save_images()

    scraper = GoogleImageScrapper(search_term, increment=int(scraper.increment)+1)


print("\n==============\n")

print(f"Scraping complete. Images Scraped: {scraper.number_existing_files}")