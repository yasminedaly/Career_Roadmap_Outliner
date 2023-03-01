#Web Scraping with Scrapy: W3Schools Tutorials
This project uses Scrapy, a Python library for web scraping, to scrape the tutorial titles and links for all the tutorials on W3Schools.

Prerequisites
To run this code, you'll need to have Scrapy installed. You can install Scrapy using pip by running the following command:

Copy code
pip install scrapy
Running the Code
To run the code, navigate to the project directory in the terminal and run the following command:

lua
Copy code
scrapy crawl wspider -o output.json
This will start the spider and save the output to a JSON file named output.json.

Code Overview
The WspiderSpider class defines the spider. The spider starts by visiting the W3Schools homepage, and then follows all the category links on the page. For each category page, the spider selects all the tutorial links and extracts the tutorial title and link.

The extracted data is then yielded to the Scrapy output pipeline, which writes the data to a JSON file.

The parse() method is called for each page visited by the spider. It uses XPath selectors to extract the category name and link from each category link on the page. It then follows the category link by making a new request using scrapy.Request().

The parse_category() method is called for each category page visited by the spider. It extracts the category name from the meta data, which was passed along from the parse() method. It then uses XPath selectors to extract the tutorial title and link from each tutorial link on the page. Finally, it yields the extracted data to the Scrapy output pipeline.

The output pipeline writes the extracted data to a JSON file specified by the -o option when running the spider.
