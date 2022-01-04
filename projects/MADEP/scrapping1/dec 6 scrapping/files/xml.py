import scrapy
from scrapy import item
from scrapy.spiders import XMLFeedSpider
from


class CoolSpider(XMLFeedSpider):
    name = 'website.com'
    allowed_domains = ['website.com']
    start_urls = ['hhtp://www.website.com/products.xml']
    itertag = 'product'

    def parse_node(self, response, node):
        item = 

