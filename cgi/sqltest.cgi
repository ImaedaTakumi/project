#!/usr/bin/python3 --
import cgi
import MySQLdb
import os
from http import cookies
import sensin
import datetime

## main program ###
text = []
error = {}
form = cgi.FieldStorage()
# reading cookie
cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE',''))
try:
	session_key = cookie["session_key"].value
except KeyError:
	session_key = ""
	
sql = f"select `session_id` from Session where session_key = '{session_key}'"
cookielogin = sensin.connection_MySQL(sql,"r","hotel")

if cookielogin:
	#cookie login sucsess
	text.append("<li><a>ログイン中</a></li>")
else:
	text.append("")

reservation_day = "2022-5-11"
sql = "select * from Room as R where R.Room_plan_id = 1 and not exists(select * from (select * from Reservation where '{reservation_day}' between Lodging_start and Lodging_end) as Twhere R.Room_id = T.Room_id);"
result = sensin.connection_MySQL(sql,"r","hotel")
print("Content-Type: text/html\n")
print(f"{result}")
