from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose


class AirbnbItem(Item):
	#Item que queremos obtener
	tipo = Field()
	capacidad = Field()

#Se define el Spider
class AirbnbCrawler(CrawlSpider):
	name = "MiPrimerCrawler"
	start_urls = ["http://www.airbnb.com/s/Londres--Reino-Unido"]

	#Evita que nos salgamos del dominio, como publicidad u otros dominios
	#Dominios especificos que se aceptan
	allowed_domains = ['airbnb.com']

	#Regla para que el spider realice el carwling horizontal
	rules = (
		#Expreciones regulares, reglas que se deben cumplir	
		
		#crawling horizontal
		Rule(LinkExtractor(allow=r'page=')),
		
		#crawling vertical
		#El callback es para que se relice la busqueda solo en esta url y no en la anteriror
		Rule(LinkExtractor(allow=r'/rooms'), callback = 'parse_items'),		

	)

	def parse_items(self,response):
		item = ItemLoader(AirbnbItem(), response)
		item.add_xpath('tipo', '/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/text()')
		item.add_xpath('capacidad', '/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[1]/div/div/div/div/div/div[1]/div[2]/span[1]/text()')
		yield item.load_item()
