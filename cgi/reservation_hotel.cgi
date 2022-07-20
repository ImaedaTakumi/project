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
			#POST
			# 色々判定できる
			# ここではとりあえず全ての項目が埋まっているかでチェック
			hotel = form.getfirst("hotel")
			plan = form.getfirst("plan")
			day = form.getfirst("day")
			adult = form.getfirst("adult")
			child = form.getfirst("child")
			food = form.getfirst("food")
			pay = form.getfirst("pay")
			memo = form.getfirst("memo")
			
			text.extend([hotel,plan])

			if None in text or "" in text:
				#全ての項目を入力していない場合
				sensin.htmlpage("../html/reservation_hotel.html",text=text,error={"error":"全ての項目を入力してください<br>"})
			else:
				#全ての項目を入力した場合
				#予約できるか判定
				try:
					reservation_day = day
					sql = f"select (`Room_plan_id`) from Room_plan where `Room_plan_name` = '{plan}'"
					plan_result = sensin.connection_MySQL(sql,"r","hotel")
					room_plan_id = plan_result[0][0]
					
					#予約したplan_idの部屋を検索
					sql = f"select * from Room as R where R.`Room_plan_id` = {room_plan_id} and not exists(select * from (select * from Reservation where '{reservation_day}' between `Lodging_start` and `Lodging_end`) as T where R.`Room_id` = T.`Room_id`);"
					result = sensin.connection_MySQL(sql,"r","hotel")

					if result:
						#成功画面を表示
						text.extend([day,adult,child,food,pay,memo])
						sensin.htmlpage("../html/reservation_confirm.html",text=text)
					else:
						sensin.htmlpage("../html/reservation_hotel.html",text=text,error={"error":"その時間帯は空いていませんでした<br>"})

				except Exception as e:
					sensin.htmlpage("../html/reservation_hotel.html",text=text,error={"error":f"不明なエラー 管理者に連絡してください {e}<br>"})
else:
	# login failed
	print("Location:../cgi/login.cgi\n")
