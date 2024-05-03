from time import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://quotes.toscrape.com/login')
    print(page.title())

    page.fill('input[name="username"]', 'admin')
    page.fill('input[name="password"]', 'admin')
    page.click('.btn.btn-primary')
    page.wait_for_load_state('load')
    if "Logout" in page.content():
        while True:
            quotes = page.query_selector_all('.quote')
            for quote in quotes:
                text = quote.query_selector('.text').text_content()
                author = quote.query_selector('.author').text_content()
                tags = [tag.text_content() for tag in quote.query_selector_all('.tag')]
                print(text, author, tags)
            next_link = page.query_selector('.next a')
            if next_link:
                next_link.click()
                page.wait_for_load_state('load')
            else:
                break


    # sleep(2)
    browser.close()
