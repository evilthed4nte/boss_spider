# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # job-primary
    # div.job-title -职位名称
    title = scrapy.Field()
    # span.red 薪水
    salary = scrapy.Field()
    # div.detail-top-text -公司名称 和 hr
    company = scrapy.Field()
    # div.detail-bottom-text br -职位描述
    description = scrapy.Field()
    # div.job-primary p
    area = scrapy.Field()
    # em.vline [1]
    work_year = scrapy.Field()
    # em.vline [2]
    education = scrapy.Field()
    # div.company-text p
    company_info = scrapy.Field()
    # 城市
    city = scrapy.Field()