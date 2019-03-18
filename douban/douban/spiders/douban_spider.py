# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
    name = "douban_spider"
    allowed_domains = ["movie.douban.com"]
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        # print(response.text)
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for i_item in movie_list:
            douban_item = DoubanItem()
            douban_item['serial_number'] = i_item.xpath(".//div[@class='item']/div/em/text()").extract_first()
            douban_item['movie_name'] = i_item.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
            douban_item['star'] = i_item.xpath(".//span[@class='rating_num']/text()").extract()
            douban_item['introduce'] = i_item.xpath(".//div[@class='bd']/p[1]/text()").extract()
            douban_item['evaluate'] = i_item.xpath(".//div[@class='star']/span[4]/text()").extract()
            douban_item['descript'] = i_item.xpath(".//p[@class='quote']/span/text()").extract()
            yield douban_item
        # next_link 下一页解析
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            next_link = response.urljoin(next_link)
            yield scrapy.Request(next_link, callback=self.parse)
