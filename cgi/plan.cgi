#!/usr/bin/python3 --
import cgi
import MySQLdb
import os
from http import cookies
import sensin
		
### main program ###

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
	with open("../html/plan.html",mode="r",encoding="utf-8") as html:
		lines = html.readlines()
	lines.insert(19, "<li><a>ログイン中</a></li>")
	with open("../html/plan.html",mode="w",encoding="utf-8") as tmp:
		tmp.writelines(lines)
	with open("../html/plan.html",mode="r",encoding="utf-8") as tmp:
		print("Content-Type: text/html\n")
		print(tmp.read())

else:
	with open("../html/plan.html",mode="r",encoding="utf-8") as html:
		print("Content-Type: text/html\n")
		print(html.read())