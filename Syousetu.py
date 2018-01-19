from scrapy import Spider
from scrapy.http import Response, Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re

class mySpider(CrawlSpider):
    name = 'Syousetu'
    allowed_domains = ["ncode.syosetu.com"]
    start_urls = ['http://ncode.syosetu.com/n2267be/1/']
    rules = [
        Rule(LinkExtractor(allow=['/n2267be/\d*']), callback='parse_item',
             follow=True)

    ]
    def parse_item(self, response):
        info = str(response.body, 'utf-8')
        A = re.findall("レム", info)
        filename = 'rem.txt'
        with open(filename, 'a') as f:
            f.write(+str(len(A))+"\n")

