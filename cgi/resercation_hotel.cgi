#!/usr/bin/python3 --
import cgi
import MySQLdb
import os
from http import cookies
import sensin

### main program ###
text = []
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
	text.append("<li><a>ログイン中</a></li>")
else:
	text.append("")

if form.list == []:
	#GET
	#getで来たらreservation.html
	sensin.htmlpage("../html/reservation.html")
else:
	#POST
	# 色々判定できる
	# ここではとりあえず全ての項目が埋まっているかでチェック
	hotel = form.getfirst("hotel")
	plan = form.getfirst("plan")
	day = form.getfirst("day")
	adult = form.getfirst("adult")
	child = form.getfirst("child")
	room = form.getfirst("room")
	dish = form.getfirst("dish")
	pay = form.getfirst("pay")
	memo = form.getfirst("memo")
	text=[hotel,plan,day,adult,child,room,dish,pay,memo]

	if "" in text:
		sensin.htmlpage("../html/reservation_hotel.html",text=[hotel,plan],error={"error":"全ての項目を入力してください<br>"})
	else:
		
		sensin.htmlpage("../html/reservation_confirm.cgi",text=text)
