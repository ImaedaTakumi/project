#!/usr/bin/python3 --
import cgi
import MySQLdb
import os
from http import cookies
import sensin
import datetime

### main program ###
text = []
error = {}
form = cgi.FieldStorage()
# reading cookie
cookielogin = sensin.read_cookie()

if cookielogin:
	#cookie login sucsess
	mail_address = cookielogin[0][0]
	text.append(f"<li><a class='abs_success'>{mail_address}ログイン中</a></li>")
	if form.list == []:
		#GET
		#getで来たらreservation.html
		sensin.htmlpage("../html/reservation.html",text=text)
	else:
		#POST
		# 色々判定できる
		# ここではとりあえず全ての項目が埋まっているかでチェック
		hotel = form.getfirst("hotel")
		plan = form.getfirst("plan")

		text.extend([hotel,plan])

		if None in text or "" in text:
			sensin.htmlpage("../html/reservation.html",text=text,error={"error":"全ての項目を入力してください<br>"})
		else:
			#予約できる日付を渡す
			#今日から30日後までの日付
			today = datetime.date.today()
			for i in range(1,30):
				daydelta = datetime.timedelta(i)
				date = today + daydelta
			
			sensin.htmlpage("../html/reservation_hotel.html",text=text)
else:
	# login failed
	print("Location:../cgi/login.cgi\n")
	

