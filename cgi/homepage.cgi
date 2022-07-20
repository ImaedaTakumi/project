#!/usr/bin/python3 --
import cgi
import MySQLdb
import os
from http import cookies
import sensin

		
### main program ###

# reading cookie
text = []
cookielogin = sensin.read_cookie()

if cookielogin:
	#cookie login sucsess
	text.append("<li><a class='abs_success'>ログイン中</a></li>")
else:
	text.append("")

sensin.htmlpage("../html/homepage.html",text=text)