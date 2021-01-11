from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector

#Realizaremos un scraping buscando las preguntas del inicio en stackoverflow

#Lo ejecutamos a travez de consola con:
# $scrapy runspider my_first_spider.py -o stackoverflow.csv -t csv


class Pregunta(Item):
	pregunta = Field()
	id = Field()

class StackOverflowSpider(Spider):
	
	name = "MiPrimerSpider"

	#URL a la cual relaizaremos scraping
	start_urls = ['http://es.stackoverflow.com']

	def parse(self,response):
		sel = Selector(response)

		#Direccion de la seccion donde se encuentra la pregunta
		preguntas = se.xpath('/html/body/div[4]/div[2]/div/div[1]/div[3]/div/div[2]')
		
		#Recorremos las preguntas y las almacenamos 
		for i,elem in enumerate(preguntas):
			item = ItemLoader(Pregunta(),elem)
			item.add_xpath('pregunta','/html/body/div[4]/div[2]/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/h3/a/text()')
			item.add_value('id',i)
			yield item.load_item()
