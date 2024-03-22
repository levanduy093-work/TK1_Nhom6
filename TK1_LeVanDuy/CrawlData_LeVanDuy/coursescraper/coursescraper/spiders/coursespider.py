import scrapy


class CoursespiderSpider(scrapy.Spider):
    name = "coursespider"
    allowed_domains = ["www.coursera.org"]
    start_urls = ["https://www.coursera.org/certificates/computer-science-it"]

    custom_settings = {
        'FEEDS': {
            'LeVanDuy.json': {'format': 'json', 'overwrite': True},
            'LeVanDuy.csv': {'format': 'csv', 'overwrite': True},
        }
    }

    def parse(self, response):
        courses = response.css('.ProductOfferingCard')
        for course in courses:
            relative_url = course.css('a ::attr(href)').get()
            course_url = relative_url
            yield response.follow(course_url, callback = self.parse_course_page)

    def parse_course_page(self, response):
        lectures = response.css('ul.css-7avemv li .unified-CML span ::text')
        reviews = response.css('.css-3nq2m6 .css-lt1dx1 .css-h1jogs ::text')
        if lectures and reviews:
            yield {
            'url': response.url,
            'name': response.css('h1.cds-Typography-base ::text').get(),
            'language': response.css('.css-ddn3zj ::text').get(),
            'description': response.css('.css-kd6yq1 ::text').get(),
            'instructors': response.css('.css-guxf6x a span ::text').get(),
            'learns': lectures.getall(),
            'level': reviews[1].get(),
            'time': reviews[2].get()
        }