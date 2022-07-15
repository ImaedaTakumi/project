#!/usr/bin/python3 --
import cgi
import MySQLdb
import random, string

def get_random_str(no):
	char_data = string.digits + string.ascii_lowercase + string.ascii_uppercase
	return ''.join([random.choice(char_data) for i in range(no)])

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
import crypt
error = {}
form = cgi.FieldStorage()

if form.list == []:
	#GET
	with open("../html/login.html",mode="r",encoding="utf-8") as html:
		print("Content-Type: text/html\n")
		print(html.read())
else:
	#POST
	mail_address = form.getfirst('mail_address')
	password = form.getfirst('password')

	#error
	error = {}
	if not mail_address:
		error["mail_address"] = "メールアドレスを入力してください"
	if not password:
		error["password"] = "パスワードを入力してください"


	if error == []:
		# mail/password check
		sql = f"select (`Account_id`) from Account where Mail_address = '{mail_address}' and Password = '{password}'"
		result = connection_MySQL(sql,"r","hotel")

		if result:
			#login success
			account_id = result[0]
			session_key = get_random_str(64)
			sql = f"insert into Session (`Session_id`, Session_key, `Account_id`) values ('null','{session_key}',{account_id})"
			connection_MySQL(sql,"w","hotel")
			print("Location:./login_success.cgi\n")
		else:
			#login failed
			with open("../html/login.html",mode="r",encoding="utf-8") as html:
				print("Content-Type: text/html\n")
				print(html.read())
	else:
		#form error
		with open("../html/login.html",mode="r",encoding="utf-8") as html:
			print("Content-Type: text/html\n")
			print(html.read())




