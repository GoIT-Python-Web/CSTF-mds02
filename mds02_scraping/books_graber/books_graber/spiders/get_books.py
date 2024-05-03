import scrapy


class GetBooksSpider(scrapy.Spider):
    name = "get_books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

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
