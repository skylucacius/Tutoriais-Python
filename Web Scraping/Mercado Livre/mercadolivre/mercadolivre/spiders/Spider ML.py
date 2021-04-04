import scrapy

class MLSpider(scrapy.Spider):
    name = 'ml'
    start_urls = ["https://www.mercadolivre.com.br/ofertas?page={i}"]

    def parse(self, response, **kwargs):
        for i in response.xpath('//li[@class="promotion-item"]'):
            price = i.xpath('.//span[@class="promotion-item__price"]//text()').getall()
            title = i.xpath('.//p[@class="promotion-item__title"]//text()').get()
            link = i.xpath('.//a[@href="https://produto.mercadolivre.com.br/MLB-1820104290-oximetro-digital-de-dedo-medidor-de-saturaco-de-oxignio-_JM?hide_psmb=true#reco_item_pos=0&reco_backend=promotions-sorted-by-score-mlb-A&reco_backend_type=low_level&reco_client=seller-promotions&reco_id=e262037e-ac02-4ada-bb57-740de8a32a2d&deal_print_id=eb1a184b-5cac-490e-84c3-7230d1f4d659&model_version=recommendations/prueba-promotions-MLB__3551__KAKUY&promotion_type=DEAL_OF_THE_DAY"]')
            
            yield {
                'price' : price,
                'title' : title,
                'link' : link
           }

        next_page = response.xpath('//a[contains(@title,"Próxima")]/@href').get()
        if next_page:
            yield scrapy.Request(next_page,self.parse)