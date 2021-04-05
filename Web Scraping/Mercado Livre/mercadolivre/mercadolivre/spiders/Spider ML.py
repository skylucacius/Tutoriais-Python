import scrapy

class MLSpider(scrapy.Spider):
    name = 'ml'
    start_urls = ["https://www.mercadolivre.com.br/ofertas?page={i}"]

    def parse(self, response):
        for i in response.xpath('//li[@class="promotion-item"]'):
            price = i.xpath('.//span[@class="promotion-item__price"]//text()').getall()
            title = i.xpath('.//p[@class="promotion-item__title"]//text()').get()
            link = i.xpath('.//a[@class="promotion-item__link-container"]').get()
            
            yield {
                'price' : price,
                'title' : title,
                'link' : link
           }

        next_page = response.xpath('//a[contains(@title,"Próxima")]/@href').get()
        if next_page:
            # yield scrapy.Request(next_page,self.parse)
            yield response.follow(next_page, self.parse)