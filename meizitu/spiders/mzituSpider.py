import scrapy

class MzituSpider(scrapy.spider.Spider):
    name="mzitu_Spider"
    allowed_domains=["mzitu.com"]
    start_urls=[
        "http://www.mzitu.com/"
    ]

    def parse(self, response):
        current_url = response.url
        body = response.body
        unicode_body = response.body_as_unicode()
        