# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class DoubanmovieItem(scrapy.Item):
    ranking = scrapy.Field()  # 电影排名
    title = scrapy.Field()  # 电影名字
    movieinfo = scrapy.Field()  # 电影介绍
    star = scrapy.Field()  # 电影评分
    movietype = scrapy.Field()  # 电影类型
    publish = scrapy.Field()  # 电影出版日期
    country = scrapy.Field()  # 电影出版国家
    pass
