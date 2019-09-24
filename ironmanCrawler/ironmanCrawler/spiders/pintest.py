# -*- coding: utf-8 -*-
import scrapy


class PintestSpider(scrapy.Spider):
    name = 'pintest'
    # allowed_domains = ['pinterest.com']
    start_urls = ['http://pinterest.com/']
    http_user = 'mrdragon0022@gmail.com'
    http_pass = 'test1234'

    def crawl(self, response):
        pass

    def parse(self, response):
        return 1
        # return scrapy.FormRequest.from_response(
        #     response,
        #     formdata={'username': 'mrdragon0022@gmail.com', 'password': 'test1234'},
        #     callback=self.after_login
        # )

    def after_login(self, response):
        if "Error while logging in" in response.body:
            self.logger.error("Login failed!")
        else:
            self.logger.error("Login succeeded!")
