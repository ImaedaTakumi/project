#!/usr/bin/python3 --
import cgi
import MySQLdb
import os
from http import cookies

from requests import Session
import sensin

### main program ###
error = {}
form = cgi.FieldStorage()
# reading cookie
cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE',''))
try:
	session_id = cookie["session_id"].value
except KeyError:
	session_id = ""
	
sql = "select `session_id` from Session where session_id = '"+session_id+"'"
cookielogin = sensin.connection_MySQL(sql,"r","hotel")

if cookielogin:
	#cookie login sucsess
	sensin.htmlpage("../html/reservation_hotel.html",text=["<li><a>ログイン中</a></li>"])
else:
	sensin.htmlpage("../html/reservation_hotel.html")