# -*- coding: utf-8 -*-
import json
import time

import scrapy

from boss.items import JobItem


class bsSpider(scrapy.Spider):
    name = 'bs'

    def __init__(self, name=None, **kwargs):
        super().__init__(name=None, **kwargs)
        self.base_url = 'https://www.zhipin.com'
        self.base_query = '/c101210100/?query=python&page=1'
        self.base_hot_city = ''

    def start_requests(self):
        url = 'https://www.zhipin.com/job_detail/?query=python&city=101210100&industry=&position='
        # url = 'https://www.zhipin.com/c101210100/?query=python&page=2&ka=page-next'

        yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        # 添加item
        item  = JobItem()

        # 写入item
        job_list = response.css('div.job-list > ul > li')
        for job in job_list:
            job_primary = job.css('div.job-primary')
            # item['title'] = job_primary.css('div.info-primary > h3 > div::text').extract_first().strip()
            item['title'] = job_primary.css('div.job-title::text').extract_first().strip()
            item['salary'] = job_primary.css('div.info-primary > h3 > a > span::text').extract_first().strip()
            item['city'] = job_primary.css('div.info-primary > p::text').extract_first().strip()
            yield item


        # print("-----神不知鬼不觉的分割线-----")
        next_page = response.css('a.next::attr(href)').extract()[0]
        if next_page is not None and next_page != 'javascript:;':
            # 拼接url
            next_page = self.base_url + next_page
            time.sleep(5)
            yield scrapy.Request(next_page, callback=self.parse)
            # print(next_page)




