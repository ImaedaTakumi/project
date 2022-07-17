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
	food = form.getfirst("dish")
	pay = form.getfirst("pay")
	memo = form.getfirst("memo")

	if "" in text:
		sensin.htmlpage("../html/reservation_confirm.html",text=text,error={"error":"不明なエラーです"})
	else:
		#色々
		# account情報取り出し
		try:
			account_id = cookielogin[0]
			sql = f"select (`Account_id`,`Credit_id`) from Account where Account_id = {account_id}"
			account_result = sensin.connection_MySQL(sql,"r","hotel")
			account_id = account_result[0][0]
			credit_id = account_result[0][1]

			sql = f"select (`Hotel_id`) from Hotel where `Hotel_id` = {hotel}"
			hotel_id = sensin.connection_MySQL(sql,"r","hotel")

			sql = f"select (`Room_id`, `Room_plan_id`) from Room where `Room_id` = {room}"
			room_result = sensin.connection_MySQL(sql,"r","hotel")
			room_id = room_result[0][0]
			room_plan_id = room_result[0][1]

			sql = f"select (`Price`) from Room_plan where `Room_plan_id` = {room_plan_id}"
			room_price = sensin.connection_MySQL(sql,"r","hotel")

			sql = f"select (`Food_id`,`Price`) from Food where `Food_id` = {food}"
			food_result = sensin.connection_MySQL(sql,"r","hotel")
			food_id = food_result[0][0]
			food_price = food_result[0][1]
			
			price = (room_price + food_price)
			lodging_start = day
			lodging_end = day
			# 予約情報書き込み
		
		
			sql = "insert (`Reservation_id`,`Account_id`,`Hotel_id`,`Room_id`,`Room_plan_id`,`Food_id`,`Adult_num`,`Child_num`,`Lodging_start`,`Lodging_end`,`Payment_info`,`Payment_price`,`Credit_id`,`Memo`) "
			sql += f"values (null,{account_id},{hotel_id},{room_id},{room_plan_id},{food_id},{adult},{child},{lodging_start},{lodging_end},{pay},{price},{credit_id},{memo})"
		except:
			sensin.htmlpage("../html/reservation_confirm.html",text=text,error={"error":"不明なエラー2です"})