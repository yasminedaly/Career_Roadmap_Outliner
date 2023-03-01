import scrapy


class courseracourseSpider(scrapy.Spider):
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
        item['title'] = response.css('.banner-title.banner-title-without--subtitle.m-b-0::text')[0].get()
        item['description'] = response.css('.rc-TogglableContent.about-section .content-inner p::text').get()
        item['inscriptions'] = response.css('._1fpiay2 span::text').get()
        item['hours'] = response.css('._16ni8zai.m-b-0.m-t-1s span::text').get()
        list = response.css('._16ni8zai.m-b-0::text').extract()
        item['language'] = list[-1] if len(list) >= 2 else None
        item['level'] = response.css('._16ni8zai.m-b-0.m-t-1s::text').get()
        item['provider'] = response.css('.headline-4-text.bold.rc-Partner__title::text').get()
        yield item
