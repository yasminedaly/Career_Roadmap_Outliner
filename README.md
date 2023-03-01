
## Coursera Scraper
This is a web scraper for Coursera that allows you to extract data on courses and projects from the website. The scraper is built using Python and the Scrapy framework.

## Installation
To install the scraper, clone the repository to your local machine:

```
git clone https://github.com/yasminedaly/Career_Roadmap_Outliner.git
```
All of the following will be built into a virtualenv

Make sure you have Python 3.x installed on your machine. You can install the required Python libraries by running:

```
pip install scrapy
```

## Usage
To use the scraper, navigate to the coursera-scraper directory then to the spiders folder  and run one of the following commands:

To scrape course data:

```
scrapy crawl courseracourseSpider -o courses.json
```

To scrape project data:

```
scrapy crawl courseraprojectSpider -o projects.json
```
The scraped data will be saved to a JSON file in the spiders directory.

## File Structure
The coursera-scraper directory has the following file structure:

items.py: defines the data structure for scraped items
middlewares.py: defines the middleware settings for the scraper
pipelines.py: defines the pipeline settings for the scraper
settings.py: defines the global settings for the scraper
spiders: a directory containing the spider classes for scraping course and project data
courseracourseSpider.py: the spider class for scraping course data
courseraprojectSpider.py: the spider class for scraping project data
courses.json: the JSON file containing scraped course data
projects.json: the JSON file containing scraped project data
