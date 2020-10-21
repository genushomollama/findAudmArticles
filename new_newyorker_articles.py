import scrapy


class NewNewyorkerArticlesSpider(scrapy.Spider):
    name = 'new_newyorker_articles'
    allowed_domains = ['newyorker.com']
    start_urls = ['https://www.newyorker.com/sitemap?year=2020&month=10&week=3']
    count = 0

    def parse(self, response):
        print("processing:" + response.url)
        first_url = response.css("li a :not(.Link__link___3dWao) ::attr(href)").extract_first() # FIXME testing remove
        if first_url is not None:
            print(first_url.text)


        if self.count == 0:
            urls = response.css("li a:not(.Link__link___3dWao) ::attr(href)").extract()
            for url in urls:
                print("Calling on ", url)
                yield scrapy.Request(url, callback=self.parse)
        else:
            print("We are on an article", response.url)  # FIXME testing remove
            iframes = response.css("iframe ::attr(src)").extract()
            for iframe in iframes: #  "audm" in  response.css("iframe ::attr(src)").extract()[0]
                if "audm" in iframe:
                    print("FOUND AUDM RECORDING:", response.url)
                    # TODO yield data? maybe in a dictionary? not really necessary for this it seems
        self.count += 1
        pass
