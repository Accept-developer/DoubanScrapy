import scrapy
import re
from scrapy.http import Request
from scrapy.selector import Selector
from doubanmovie.items import DoubanmovieItem
from urllib.parse import urljoin


class Douban(scrapy.spiders.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    # redis_key = 'douban:start_urls'
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        item = DoubanmovieItem()
        selector = Selector(response)
        Movies = selector.xpath('//ol[@class="grid_view"]/li')
        for eachMovie in Movies:
            ranking = eachMovie.xpath('.//div[@class="pic"]/em/text()').extract()[0]
            title = eachMovie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()[0]
            movieinfo = eachMovie.xpath('.//div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            star = eachMovie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            movietype = eachMovie.xpath('.//div[@class="info"]/div[@class="bd"]/p[1]/text()').extract()
            for m_type in movietype:
                movie_type = "".join(m_type.split())
                types = movie_type.split('/')
                if(len(types) == 3):
                    item['publish'] = types[0]
                    item['country'] = types[1]
                    item['movietype'] = types[2]
                else:
                    item['publish'] = types[0]
                    item['country'] = types[0]
                    item['movietype'] = types[0]

            item['ranking'] = ranking
            item['title'] = title
            #item['movieinfo'] = ';'.join(movieinfo)
            item['movieinfo'] = movieinfo
            item['star'] = star
            yield item
        nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        # 第10页是最后一页，没有下一页的链接
        if nextLink:
            nextLink = nextLink[0]
            yield Request(urljoin(response.url, nextLink), callback=self.parse)
