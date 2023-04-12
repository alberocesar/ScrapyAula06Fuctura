import scrapy


class ImdbSpider(scrapy.Spider):
    name = "imdb"
    #allowed_domains = ["exemple.com"]
    start_urls = ["https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"]

    def parse(self, response):
        for serie in response.css('.titleColumn'):
            titulo = serie.css('a::text').get()
            ano = serie.css('.secondaryInfo::text').get()[1:-1]

            # selecionar o elemento pai do elemento atual
            nota = serie.xpath('../td[@class="ratingColumn imdbRating"]//strong/text()').get()

            yield {
                'titulo': titulo,
                'ano': ano,
                'nota': nota
            }
