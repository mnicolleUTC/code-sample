import os
import logging
import scrapy
from scrapy.crawler import CrawlerProcess

def get_number_balise_next_page(current_page_number):
    # Get the number of the next page, based on the current page number
    if current_page_number in list(range(1,6)):
        next_page_number = current_page_number + 2
    if current_page_number > 5:
        next_page_number = 7
    return next_page_number

class YelpSpider(scrapy.Spider):
    name = "yelp"
    page_number = 0
    start_urls = ['https://www.yelp.fr/']

    # Parse function for form request

    def parse(self, response):
        # FormRequest used to make a search in Paris
        return scrapy.FormRequest.from_response(
            response,
            formdata={
                'find_desc': 'restaurant japonais',
                'find_loc':'Paris'
                },
            callback=self.after_search
        )

    # Callback used after login
    def after_search(self, response):
        self.page_number += 1
        for i in range(3, 13):
            xpath_name = f'/html/body/yelp-react-root/div[1]/div[4]/div/div/div[1]/main/ul/li[{i}]/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div/h3/a/text()'
            xpath_note = f'/html/body/yelp-react-root/div[1]/div[4]/div/div/div[1]/main/ul/li[{i}]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/span[1]/text()'
            xpath_number_vote = f'/html/body/yelp-react-root/div[1]/div[4]/div/div/div[1]/main/ul/li[{i}]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/span[2]/text()'
            xpath_url = f'/html/body/yelp-react-root/div[1]/div[4]/div/div/div[1]/main/ul/li[{i}]/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div/h3/a/@href' 
            
            yield {
                'name': response.xpath(xpath_name).get(),
                'note': response.xpath(xpath_note).get(),
                'number_vote': response.xpath(xpath_number_vote).get(),
                'url': response.xpath(xpath_url).get()
            }
        # Select the NEXT button and store it in next_page
        # try:
        #     next_page_number = get_number_balise_next_page(self.page_number)
            
        #     next_page = response.xpath(f'/html/body/yelp-react-root/div[1]/div[4]/div/div/div[1]/main/ul/li[13]/div/div/div[{next_page_number}]/span/a').attrib["href"]
        if self.page_number in list(range(1,11)):
            next_page_number = get_number_balise_next_page(self.page_number)
            next_page = response.xpath(f'/html/body/yelp-react-root/div[1]/div[4]/div/div/div[1]/main/ul/li[13]/div/div/div[{next_page_number}]/span/a').attrib["href"]
            logging.info('Go on next page')
            yield response.follow(next_page, callback=self.after_search)
        else:
            logging.info('No more page to crawl')
            return
        
# Name of the file where the results will be saved
filename = "all_japonais-paris.json"

# If file already exists, delete it before crawling (because Scrapy will concatenate the last and new results otherwise)
if filename in os.listdir():
        os.remove('' + filename)

# Declare a new CrawlerProcess with some settings
process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        '' + filename: {"format": "json"},
    }
})

# Start the crawling using the spider you defined above
process.crawl(YelpSpider)
process.start()