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
	mail_address = cookielogin[0][0]
	text.append(f"<li><a class='abs_success'>{mail_address}ログイン中</a></li>")
else:
	text.append("")

sensin.htmlpage("../html/homepage.html",text=text)