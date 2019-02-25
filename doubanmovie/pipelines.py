# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from doubanmovie import settings


class DoubanmoviePipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=False)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """insert into doubantop250(ranking, title, movieinfo, star, movietype, publish, country)
                  value (%s,%s,%s,%s,%s,%s,%s)""",
                (item['ranking'], item['title'], item['movieinfo'], item['star'], item['movietype'], item['publish'], item['country']))
            self.connect.commit()
        except Exception as err:
            print("重复插入了==>错误信息为：" + str(err))
        return item
