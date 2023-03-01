import scrapy


class WspiderSpider(scrapy.Spider):
    name = "wspider"
   
    start_urls = ['https://www.w3schools.com/']

    def parse(self, response):
        # Select all the category links
        for category_link in response.xpath('//a[@class="w3-bar-item w3-button"]'):
            # Get the category name and link
            category_name = category_link.xpath('text()').get().strip()
            category_url = response.urljoin(category_link.xpath('@href').get())

            # Follow the category link and select all the tutorial links
            yield scrapy.Request(category_url, callback=self.parse_category, meta={'category_name': category_name})

    def parse_category(self, response):
        # Extract the category name from the meta data
        category_name = response.meta['category_name']

        # Select all the tutorial links
        for tutorial_link in response.xpath('//a[@class="w3-bar-item w3-button"]'):
            # Get the tutorial title and link
            tutorial_title = tutorial_link.xpath('text()').get().strip()
            tutorial_url = response.urljoin(tutorial_link.xpath('@href').get())

            # Yield the data
            yield {
                'category': category_name,
                'title': tutorial_title,
                'link': tutorial_url
            }




