import scrapy


class SpiderTecnoblog(scrapy.Spider):
    name = 'tecnoblog'
    # allowed_domains = ['tecnoblog.net']
    start_urls = ['http://tecnoblog.net/']

    def parse(self, response):
        for i in response.xpath('//article'):
            link = i.xpath('.//a/@href').get()
            yield response.follow(link, self.parse_article)

    def parse_article(self, response):
        titulo = response.xpath('//h1/a/text()').get()
        conteudos = response.xpath('//p').getall()
        yield {
            'titulo' : titulo,
            'conteudos' : conteudos
        }

