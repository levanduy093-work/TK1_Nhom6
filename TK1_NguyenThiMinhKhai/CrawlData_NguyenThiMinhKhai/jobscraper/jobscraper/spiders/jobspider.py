import scrapy


class JobspiderSpider(scrapy.Spider):
    name = "jobspider"
    allowed_domains = ["www.timesjobs.com"]
    # start_urls = ["https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&txtKeywords=swift&postWeek=60&searchType=personalizedSearch&actualTxtKeywords=swift&searchBy=0&rdoOperator=OR&pDate=I&sequence=1&startPage=1"]

    custom_settings = {
        'FEEDS': {
            'data.json': {'format': 'json', 'overwrite': 'True'},
            'data.csv': {'format': 'csv', 'overwrite': 'True'},
        }
    }

    def start_requests(self):
        for page_number in range(1,11):
            yield scrapy.Request('https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&txtKeywords=swift&postWeek=60&searchType=personalizedSearch&actualTxtKeywords=swift&searchBy=0&rdoOperator=OR&pDate=I&sequence={page_number}&startPage=1'.format(page_number=page_number), callback=self.parse)

    def parse(self, response):
        jobs = response.css('ul.new-joblist li.clearfix.job-bx')
        for job in jobs:
            job_url = job.css('header.clearfix h2 a ::attr(href)').get()
            yield response.follow(job_url, self.parse_job)
    
    def parse_job(self, response):
        yield {
            'url': response.url,
            'company': response.css('.jd-sec.jd-hiring-comp span.basic-info-dtl ::text').get(),
            'website': response.css('ul.hirng-comp-oth a ::attr(href)').get(),
            'job_name': response.css('.jd-header h1.jd-job-title ::text').get(),
            'job_description': response.css('.jd-desc ul li ::text').getall(),
            'job_function': response.css('.about-jd-comp .job-basic-info span.basic-info-dtl ::text').get(),
        }
