# -*- coding: utf-8 -*-
import scrapy
from kickstarter.items import KickstarterItem
from scrapy.selector import Selector

class KickSpider(scrapy.Spider):
    name = "kick"

    def __init__(self, *args, **kwargs): 
        super(KickSpider, self).__init__(*args, **kwargs) 
        self.start_urls = [kwargs.get('start_url')] 

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html
        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        items = []

        item = KickstarterItem()
        item['name'] = sel.xpath('/html/head/title/text()').extract_first()
        items.append(item)

        return items
