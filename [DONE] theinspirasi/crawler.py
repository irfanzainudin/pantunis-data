import scrapy


class TheInspirasi(scrapy.Spider):
    name = "theinspirasi"
    start_urls = ["https://theinspirasi.my/?s=pantun"]

    def parse(self, response):
        # TODO: change this to work
        for title in response.css():
            yield title
