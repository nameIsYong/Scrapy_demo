# -*- coding: utf-8 -*-

import scrapy
import sys
from my_project.items import MyProjectItem

# sys.setdefaultencoding('utf-8')

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["http://www.mmjpg.com/"]
    start_urls = [
        "http://www.mmjpg.com/"
    ]

    def parse(self, response):
        list = response.xpath("//div[@class='pic']/ul/li")
        print '====================star==========='
        # print list;
        # for index in range(len(list)):
        for note in list:
            name = note.xpath("./a/img/@src").extract()
            title = note.xpath("./a/img/@alt").extract()
            item  = MyProjectItem();
            item['name'] = name;
            item['title'] = title;
            # print  name;
            # print title;
            print '---------------->'
            yield  item;