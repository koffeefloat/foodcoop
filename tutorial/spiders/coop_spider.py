import scrapy

from tutorial.items import CoopItem

class CoopSpider(scrapy.Spider):
    name = "coop"
    allowed_domains = ["foodcoop.com"]
    start_urls = [
        "https://www.foodcoop.com/produce"
    ]
    
    def parse(self, response):
        for sel in response.xpath('//tbody/tr'):
            item = CoopItem()

            item['name'] = sel.xpath('td[@class="col-sm-4"]/div[@class="col-sm-12 col-xs-6"]/text()').extract()
            item['price'] = sel.xpath('td[@class="col-sm-1 hidden-xs"]/text()').extract() 
            item['unit'] = sel.xpath('td[@class="col-sm-1 hidden-xs"]/div/text()').extract()
            item['is_organic'] = sel.xpath('td[@class="col-sm-2 hbasis hidden-xs"]/text()').extract()
            item['origin'] = sel.xpath('td[@class="col-sm-3 hbasis hidden-xs"]/text()').extract()

            yield item
