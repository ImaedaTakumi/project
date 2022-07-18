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
print("Content-Type: text/html\n")
print("""
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>sqltest</title>
</head>
""")

room = "紅葉プラン"
sql = f"select (`Room_plan_id`) from Room_plan where `Room_plan_name` = '{room}'"
room_result = sensin.connection_MySQL(sql,"r","hotel")
room_plan_id = room_result[0][0]

reservation_day = "2022-5-11"
sql = f"select * from Room as R where R.`Room_plan_id` = {room_plan_id} and not exists(select * from (select * from Reservation where '{reservation_day}' between `Lodging_start` and `Lodging_end`) as T where R.`Room_id` = T.`Room_id`);"
result = sensin.connection_MySQL(sql,"r","hotel")

print(f"{result}")

