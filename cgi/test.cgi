#!/usr/bin/python3 --
import cgi
from datetime import datetime
import MySQLdb
import random, string
import os ,json
import datetime
from http import cookies
import cgitb
import hashlib
import sensin
		
### main program ###
error = {}
form = cgi.FieldStorage()
cookie = sensin.CookieSession()

if form.list == []:
	#GET
	output = cookie.output()
	htmlText=f'''
	<!DOCTYPE html>
	<html lang="ja">
	<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<title>login</title>
	</head>
	<body>
	{output}
	<form action="./form1.cgi" method="post">
	氏名<input type="text" name="user_name"><br>
	住所<input type="text" name="home_address"><br>
	<input type="submit" name="submit" value="アカウント作成">
	</form>
	</body>
	'''
	print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))
else:
	#POST
	#cookieの設定
	cookie["user_name"] = form.getfirst("user_name")
	cookie["home_address"] = form.getfirst("home_address")

	#sessionの設定
	cgitb.enable()
	# 実行テスト(訪問カウンタの例)
	ck = sensin.CookieSession()
	counter = 1    
	if "counter" in ck:
		counter = int(ck["counter"]) + 1
	ck["counter"] = counter
	print("Content-Type: text/html; charset=utf-8")
	print(ck.output())
	print("")
	print("counter=",counter)

	cnt = cookie.output()
	htmlText=f"今入力したやつ{cnt}" 
	print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))

	"""
	insert into Hotel (`Hotel_id`,`Hotel_name`,`Place_name`) values (null,'片倉','東京都八王子市倉片町1111-1');
	insert into Room_plan (`Room_plan_id`,`Room_plan_name`,`Max_number`,`Price`) values (null,'ベーシックプラン',2,20000);
	insert into Room_plan (`Room_plan_id`,`Room_plan_name`,`Max_number`,`Price`) values (null,'紅葉プラン',4,40000);
	insert into Room_plan (`Room_plan_id`,`Room_plan_name`,`Max_number`,`Price`) values (null,'団体プラン',15,100000);
	insert into Room (`Room_id`,`Hotel_id`,`Room_plan_id`,`Room_name`,`Canchild`) values (null,1,1,'101号室',1);
	insert into Food (`Food_id`,`Food_name`,`Price`) values (null,'お料理1',280);
	insert into Food (`Food_id`,`Food_name`,`Price`) values (null,'お料理2',380);
	insert into Food (`Food_id`,`Food_name`,`Price`) values (null,'お料理3',480);
	insert into Food (`Food_id`,`Food_name`,`Price`) values (null,'お料理4',580);
	
	replace into Session (`Session_id`,`Session_key`,`Account_id`) values (null,"cat2",1);
	merge into Session as A
	using (select 1 as S_id, "cat" as key,1 as A_id) as B
	on(A.Session_id = B.S_id)
	when matched then 
	update set `Session_key` = "334"
	when not matched then
	insert (`Session_id`,`Session_key`,`Account_id`) values (null,"cat2",1);

	"""


