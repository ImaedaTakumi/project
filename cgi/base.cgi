#!/usr/bin/python3 --
import cgi
import MySQLdb
import os
from http import cookies
import sensin
		
### main program ###

# reading cookie
cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE',''))
try:
	session_id = cookie["session_id"].value
except KeyError:
	session_id = ""
text = []
sql = "select `session_id` from Session where session_id = '"+session_id+"'"
cookielogin = sensin.connection_MySQL(sql,"r","hotel")

if cookielogin:
	#cookie login sucsess
	text.append("<li><a class='abs_success'>ログイン中</a></li>")
	sensin.htmlpage("../html/dish.html",text=text)
else:
	sensin.htmlpage("../html/dish.html")
