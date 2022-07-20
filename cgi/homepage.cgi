#!/usr/bin/python3 --
import cgi
import MySQLdb
import os
from http import cookies
import sensin

		
### main program ###

# reading cookie
text = []
cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE',''))
try:
	session_key = cookie["session_key"].value
except KeyError:
	session_key = ""
	
sql = f"select `Account_id` from Session where Session_key = '{session_key}'"
cookielogin = sensin.connection_MySQL(sql,"r","hotel")

if cookielogin:
	#cookie login sucsess
	text.append("<li><a class='success'>ログイン中</a></li>")
else:
	text.append("")

sensin.htmlpage("../html/homepage.html",text=text)