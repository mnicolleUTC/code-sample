import os
import logging
import scrapy
from scrapy.crawler import CrawlerProcess

class YelpSpider(scrapy.Spider):
    # Name of your spider
    name = "yelp"

    # Starting URL
    start_urls = ['https://www.yelp.fr/']

    # Parse function for form request
    def parse(self, response):
        # FormRequest used to make a search in Paris
        # https://www.yelp.fr/search?find_desc=restaurant+japonais&find_loc=Paris
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
            
# Name of the file where the results will be saved
filename = "page1_japonais-paris.json"

# If file already exists, delete it before crawling (because Scrapy will concatenate the last and new results otherwise)
if filename in os.listdir():
        os.remove('' + filename)

# Declare a new CrawlerProcess with some settings
process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/110.0.5481.78',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {'' + filename: {"format": "json"},
    }
})

# Start the crawling using the spider you defined above
process.crawl(YelpSpider)
process.start()