# -*- coding: utf-8 -*-
import scrapy


class WhatsappSpider(scrapy.Spider):
    name = 'whatsapp'
    allowed_domains = ['play.google.com']
    start_urls = ['http://play.google.com/']

    def parse(self, response):
        pass
