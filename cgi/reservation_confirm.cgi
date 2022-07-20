#!/usr/bin/python3 --
import cgi
from typing import Type
import MySQLdb
import os
from http import cookies
import sensin

### main program ###
text = []
error = {}
form = cgi.FieldStorage()

# reading cookie
cookielogin = sensin.read_cookie()

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
		food = form.getfirst("food")
		pay = form.getfirst("pay")
		memo = form.getfirst("memo")
		text.extend([hotel,plan,day,adult,child,food,pay,memo])

		if None in text or "" in text:
			sensin.htmlpage("../html/reservation_confirm.html",text=text,error={"error":"不明なエラーです<br>"})
		else:
			#色々
			# account情報取り出し
			try:
				account_id = cookielogin[0][0]
				sql = f"select `Account_id`,`Credit_id` from Account where Account_id = {account_id}"
				account_result = sensin.connection_MySQL(sql,"r","hotel")
				account_id = account_result[0][0]
				credit_id = account_result[0][1]

				sql = f"select `Hotel_id` from Hotel where Hotel_name = '{hotel}'"
				hotel_result = sensin.connection_MySQL(sql,"r","hotel")
				hotel_id = hotel_result[0][0]

				sql = f"select `Room_plan_id` from Room_plan where Room_plan_name = '{plan}'"
				plan_result = sensin.connection_MySQL(sql,"r","hotel")
				room_plan_id = plan_result[0][0]

				#予約したplan_idの部屋を検索
				reservation_day = day
				sql = f"select `Room_id`,`Room_plan_id` from Room as R where R.Room_plan_id = {room_plan_id} and not exists(select * from (select * from Reservation where '{reservation_day}' between Lodging_start and Lodging_end) as T where R.Room_id = T.Room_id);"
				room_result = sensin.connection_MySQL(sql,"r","hotel")
				room_id = room_result[0][0]
				room_plan_id = room_result[0][1]

				sql = f"select `Price` from Room_plan where `Room_plan_id` = {room_plan_id}"
				room_price_result = sensin.connection_MySQL(sql,"r","hotel")
				room_price = room_price_result[0][0]

				sql = f"select `Food_id`,`Price` from Food where `Food_name` = '{food}'"
				food_result = sensin.connection_MySQL(sql,"r","hotel")
				food_id = food_result[0][0]
				food_price = food_result[0][1]
				
				if pay == "クレジットカード":
					pay_info = 0
				else:
					pay_info = 1
				
				price = (room_price + food_price)
				lodging_start = day
				lodging_end = day

				# 予約情報修正
				if credit_id == None:
					credit_id = "Null"
				if memo == None:
					memo = ""
				
				# 予約情報書き込み
			
				sql = "insert into Reservation (`Reservation_id`,`Account_id`,`Hotel_id`,`Room_id`,`Room_plan_id`,`Food_id`,`Adult_num`,`Child_num`,`Lodging_start`,`Lodging_end`,`Payment_info`,`Payment_price`,`Credit_id`,`Memo`)"
				sql += f"values (null,{account_id},{hotel_id},{room_id},{room_plan_id},{food_id},{adult},{child},'{lodging_start}','{lodging_end}',{pay_info},{price},{credit_id},'{memo}')"
				sensin.connection_MySQL(sql,"w","hotel")

				# 予約成功
				sensin.htmlpage("../html/reservation_success.html",text=text)
			
			except Exception as e:
				sensin.htmlpage("../html/reservation_confirm.html",text=text,error={"error":f"不明なエラー2です {e}<br>"})
else:
	# login failed
	print("Location:../cgi/login.cgi\n")
