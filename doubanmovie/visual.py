import pymysql
from pyecharts import Line
from pyecharts import Bar

from pyecharts import Pie
#message = 'The quick brown fox jumps over the lazy dog'
#count = {}
#for character in message:
#    count.setdefault(character, 0)
#    count[character] = count[character]+1
#
#print(count)
config = {
    'host': "127.0.0.1",
    'user': "root",
    'password': "1021",
    'db': "doubanmovie",
    'charset': 'utf8'
}
conn = pymysql.connect(**config)
#conn = pymysql.connect(host='127.0.0.1', port='3306', user='root', passwd='1021', db='doubanmovie', charset='utf8')
cur = conn.cursor()
cur.execute('select publish,star from doubantop250')
#result1 = cur.fetchall()
publishCount = {}
starCount = {}
for publish, star in cur.fetchmany(size=250):
    publishCount.setdefault(publish, 0)
    publishCount[publish] = publishCount[publish] + 1
    starCount.setdefault(star, 0)
    starCount[star] = starCount[star] + 1
print(publishCount)
print(sorted(publishCount.keys()))
publishDict = dict(sorted(publishCount.items(), key=lambda item: item[0]))
print(publishDict)
print(publishCount.values())
print(starCount.values())
cur.close()
conn.close()

attr = list(publishDict.keys())
v2 = list(publishDict.values())
score = list(starCount.keys())
newScore = list(reversed(score))
scoreCount = list(starCount.values())
newScoreCount = list(reversed(scoreCount))

bar = Bar("豆瓣电影Top250上映年份统计柱形图", "")
bar.add("上映年份", attr, v2)
bar.show_config()
bar.render('./html/scatter01.html')

line = Line("豆瓣电影Top250评分统计折线图")
line.add("豆瓣评分", newScore, newScoreCount, is_smooth=True, mark_line=["max", "average"])
line.show_config()
line.render('./html/scatter02.html')
