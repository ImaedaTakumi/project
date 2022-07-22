#!/usr/bin/python3 --
import cgi
import sensin
import crypt
import os

form = cgi.FieldStorage()
title = form.getfirst('title')
author = form.getfirst('author')
article = form.getfirst('article')

if(title is not None and author is not None and article is not None):
	sql = "insert into `Kuchikomi` (`article_id`, `title`, `author`, `article_comment`) values (null, '" + title + "', '" + author + "', '" + article + "')"

sql = "select * from Kuchikomi"
kuchikomi_arr = connection_MySQL(sql, "r", "hotel")
sensin.htmlpage("../html/kuchikomi.html")

for kuchikomi in (reversed(kuchikomi_arr)):
        htmlText = '''
        <div><strong>%s</strong><br><em>%s</em><br><br>%s</div><hr>
        '''%(kuchikomi[1], kuchikomi[2], kuchikomi[3])
        print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))