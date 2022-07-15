#!/usr/bin/python3 --
import cgi
import MySQLdb
import os
from http import cookies
import random, string

def get_random_str(no):
	char_data = string.digits + string.ascii_lowercase + string.ascii_uppercase
	return ''.join([random.choice(char_data) for i in range(no)])

#SQL接続
def connection_MySQL(sql,type,db):
	connection = MySQLdb.connect(
		host='localhost',
		user='user1',
		passwd='passwordA1!',
		db=db,
		charset='utf8'
	)
	cursor = connection.cursor()
	if type == "w" or type == "write":
		cursor.execute(sql)
		connection.commit()
		connection.close()
		return 
	if type == "r" or type == "read":
		cursor.execute(sql)
		result = cursor.fetchall()
		connection.close()
		return result
		
### main program ###

# reading cookie
cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE',''))
try:
	session_id = cookie["session_id"].value
except KeyError:
	session_id = ""
	
sql = "select `session_id` from Session where session_id = '"+session_id+"'"
cookielogin = connection_MySQL(sql,"r","hotel")

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