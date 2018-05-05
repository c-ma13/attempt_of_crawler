# -*- coding: utf-8 -*-
#get the comments of a book in douban.com and save it in a text file
#I learn it in the answer made by 'DataCastle' in the question: '如何入门 Python 爬虫？''https://www.zhihu.com/question/20899988'
"""
Created on Sat May  5 15:31:31 2018

@author: MaChao
"""
import requests
from lxml import etree
import pandas as pd
import time
import math

douban_book_web_id=1257218 #The Universe in a Nutshell
douban_book_name='TheUniverseInANutshell'

url='https://book.douban.com/subject/{}/comments/'.format(douban_book_web_id)

r = requests.get(url).text
s=etree.HTML(r)
files=s.xpath('//*[@id="comments"]/ul/li/div[2]/p/text()')
f=pd.DataFrame(files)
#get the comments of the first page

total_comments = s.xpath('//*[@id="total-comments"]/text()')
s=total_comments[0]
nums=int(s[4:-2])
#get the total number of comments

for a in range(2,math.ceil(nums/20)+1):
	url='https://book.douban.com/subject/{}/comments/hot?p={}'.format(douban_book_web_id,a)
	r = requests.get(url).text
	s=etree.HTML(r)
	files=s.xpath('//*[@id="comments"]/ul/li/div[2]/p/text()')
	f1=pd.DataFrame(files)
	f=pd.concat([f,f1],ignore_index=True)
	time.sleep(10)
	print(a,'/',math.ceil(nums/20))

f.to_csv('comments_of_{}.txt'.format(douban_book_name),header=False)


