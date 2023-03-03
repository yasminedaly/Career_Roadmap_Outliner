from scrapy import Spider, Request
from urllib.parse import urlencode


class MySpider(Spider):
    name = 'dcspider'
    start_urls = [
        'https://www.datacamp.com/search?q=&tab=courses&facets%5Btechnology%5D%5B%5D=Python'
    ]

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        params = {
            'api_key': 'YOUR_API_KEY',
            'url': self.start_urls[0],
            'bypass': 'cloudflare',
        }
        url = 'https://proxy.scrapeops.io/v1/?{}'.format(urlencode(params))
        yield Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        for course in response.css('div#courses article.dc-card.dc-card--bordered.dc-card--interactive.dc-global-search-result'):
            yield {
                'title': course.css('h4::text').get(),
                # 'description': course.css('p.dc-u-mv-8::text').get(),
                'url': response.urljoin(course.css('a::attr(href)').get()).replace('https://proxy.scrapeops.io', 'https://www.datacamp.com')
            }
