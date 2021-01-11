from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import Join
from bs4 import BeautifulSoup

class ElPaisItem(Item):
	titulo = Field()
	cointenido = Field()

class ElPaisCrawler(CrawlSpider):
	name = 'elpaiscrawler'
	allowed_domains = ['elpais.com']
	start_urls = ['https://elpais.com/noticias/paginas-web']
	
	rules = (
		#Crawling Horizontal
		Rule(LinkExtractor(allow=r'/noticias/paginas-web/\d+'),follow=True),
		#Crawling Vertical
		Rule(LinkExtractor(allow=r'/elpais/'), follow =True, callback = 'parce_items')
		)

	def parse_items(self,response):
		item = scrapy.loader.ItemLoader(ElPaisItem(),response)
		item.add_xpath('titulo', '//*[@id="articulo-titulo"]/text()')
		

		soup = BeautifulSoup(response.doby)
		
		article = soup.find(id="articulo_contenedor")
		contenido = article.text
		item.add_value('contenido',contenido)
		yield item.load_item()
