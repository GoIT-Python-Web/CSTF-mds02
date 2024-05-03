import scrapy
from itemadapter import ItemAdapter
from scrapy.crawler import CrawlerProcess


class BooksGraberPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        adapter['rating'] = adapter['rating'].replace('One', '1').replace('Two', '2').replace('Three', '3').replace(
            'Four', '4').replace('Five', '5')
        return item

class GetBooksSpider(scrapy.Spider):
    name = "get_books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]
    custom_settings = {
        "FEEDS": {"books_scrapy.csv": {"format": "csv", "overwrite": True}},
        "FEED_EXPORT_ENCODING": "utf-8",
        "ITEM_PIPELINES": {BooksGraberPipeline: 300},
    }

    def parse(self, response, **kwargs):
        cards = response.css("article.product_pod")
        for card in cards:
            yield {
                "title": card.css("h3 a::attr(title)").get(),
                "link": card.css("h3 a::attr(href)").get(),
                "price": card.css("p.price_color::text").get(),
                "thumbnail": card.css("img::attr(src)").get(),
                "rating": card.css("p.star-rating::attr(class)").get()[12:]
            }
        next_link = response.css("li.next a::attr(href)").get()
        if next_link:
            yield response.follow(next_link, callback=self.parse)


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(GetBooksSpider)
    process.start()

# Якщо хочемо отримати результати в скрипті то https://github.com/jschnurr/scrapyscript

# https://stackoverflow.com/questions/5851213/crawling-with-an-authenticated-session-in-scrapy
