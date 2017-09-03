# -*- coding: utf-8 -*-

import scrapy
import sys
import urllib
import os

from my_project.items import MyProjectItem

#写入文件
def downPic(url):
    fileName = url[-8:]
    local = "down_images/"+fileName
    if not os.path.exists(fileName):
        urllib.urlretrieve(url, local)

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["http://www.mmjpg.com/"]
    start_urls = ["http://www.mmjpg.com/"]

    def parse(self, response):
        list = response.xpath("//div[@class='pic']/ul/li")
        print '====================star==========='
        # print list;
        # for index in range(len(list)):
        for note in list:
            url = note.xpath("./a/img/@src").extract()
            title = note.xpath("./a/img/@alt").extract()
            item  = MyProjectItem();
            item['name'] = url;
            item['title'] = title;
            downPic(url[0]);
            yield  item;