import scrapy

class QuoteSpider3(scrapy.Spider):
    name = 'quote3'
    start_urls = ['http://quotes.toscrape.com/page/1/', 'http://quotes.toscrape.com/page/2/']
    
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'texto': quote.css('span.text::text').get(),
                'autor': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall()
            }
