# -*- coding: utf-8 -*-
import scrapy

class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    
    def parse(self, response):
        quotes = response.css('.author::text').extract()
        texts = response.css('.text::text').extract()
        
        for item in zip(quotes,texts):
            #create a dictionary to store the scraped info
            scraped_info = {
                'Authors' : quotes,
                'Quote' : texts,
            }
                
                #yield or give the scraped info to scrapy
            yield scraped_info
