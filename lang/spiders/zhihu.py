# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.http.cookies import CookieJar
import sys
import io
from ..items import LangItem
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/people/ming-zi-zong-shi-hen-nan-qi/following']

    def parse(self, response):
        a=Selector(response=response).xpath('//span[@class="ProfileHeader-name"]/text()').extract()
        b = Selector(response=response).xpath('//span[@class="RichText ztext ProfileHeader-headline"]/text()').extract()
        c=Selector(response=response).xpath('//div[@class="Profile-sideColumnItemValue"]/text()').extract()
        item_obj=LangItem(a=a,b=b,c=c)
        yield item_obj
        url_list=Selector(response=response).xpath('//a[@class="UserLink-link"]/@href').extract()
        for url in url_list:
            print(url)
            yield Request(
                url="https:"+url+"/following",
                method="GET",
                headers={
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
                },
                callback=self.parse,
            )
