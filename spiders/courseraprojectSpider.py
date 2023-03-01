import scrapy


class courseraSpider(scrapy.Spider):
    name = "coursera"
    
    def start_requests(self):
        for page_number in range(1,303):
            url = f'https://www.coursera.org/directory/courses?page={page_number}'

            yield scrapy.Request(
                url=url,
                callback = self.parse_urls,
                meta = {
                    'url': url
                }
            )

    def parse_urls(self, response):
        courses = response.css('.cds-33.cds-167.cds-169.css-h830z8.cds-56')


        for course in courses:
            item_url = f'https://www.coursera.org{course.css("a::attr(href)").get()}'
            title = course.css('.cds-33.cds-167.cds-169.css-h830z8.cds-56::text').get()
            
            yield scrapy.Request(
                    url = item_url,
                    callback=self.parse
                )


    def parse(self, response):
        item = {}
        item['title'] = response.css('.cds-33.css-1b0z9wy.cds-35::text').get()
        item['description'] = response.css('.cds-33.css-ngtbbz.cds-35::text').get()
        #item['inscriptions'] = response.css('._1fpiay2 span::text').get()
        item['hours'] = response.css('.cds-33.css-s6kthz.cds-35::text').get()
        item['language'] = response.css('.cds-33.css-s6kthz.cds-35::text')[4].get()
        item['level'] = response.css('.rc-TooltipWrapper.css-swgsih span::text').get()
        item['provider'] = response.css('.cds-33.css-10vfk66.cds-35::text').get()
        yield item
