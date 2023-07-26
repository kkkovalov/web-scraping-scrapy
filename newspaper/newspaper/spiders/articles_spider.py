from pathlib import Path

import scrapy

class ArticleSpider(scrapy.Spider):
    name = 'articles'
    
    def start_requests(self):
        base_url = 'https://www.vancouverislandfreedaily.com/business/pages/'
        for page_num in range(2,10):
            url = base_url + str(page_num)
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")