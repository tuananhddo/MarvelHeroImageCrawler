# -*- coding: utf-8 -*-
import scrapy

from ..items import MyItem


class BrickSpider(scrapy.Spider):
    name = 'brick'
    pageIterator = 1
    numberOfPage = 3

    # allowed_domains = ['brickset.com/sets/year-2016']
    start_urls = ['http://brickset.com/sets/year-2016/']

    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'h1 ::text'
            IMAGE_SELECTOR = 'img ::attr(src)'
            image_url = brickset.css(IMAGE_SELECTOR).extract_first()
            absolute_url = response.urljoin(image_url)
            item = MyItem()
            item['image_urls'] = [absolute_url]
            yield item
        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page and self.pageIterator < self.numberOfPage:
            self.pageIterator += 1
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
            print(self.pageIterator)

