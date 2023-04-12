import scrapy


class ForbesSpider(scrapy.Spider):
    name = "forbes"
    #allowed_domains = ["exemple.com"]
    start_urls = ["https://forbes.com.br/forbes-money/2023/01/as-10-marcas-mais-valiosas-do-mundo-em-2023/"]

    def parse(self, response):
        for forbes in response.css('h2~ p'):
            forbes = forbes.css('strong::text').get()
            yield {'forbes': forbes}