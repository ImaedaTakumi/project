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
mail_address = form.getfirst('mail_address')

password = form.getfirst('password')
password_conf = form.getfirst('password_conf')

user_name = form.getfirst('user_name')
home_address = form.getfirst('home_address')
gender = form.getfirst('gender')
birth_date = form.getfirst('birth_date')
credit_id = form.getfirst('credit_id')

if form.list == []:
	#GET
	with open("../html/adduser.html",mode="r",encoding="utf-8") as html:
		print("Content-Type: text/html\n")
		print(html.read())
else:
	#POST
	if not mail_address:
		error["mail_address"] = "メールアドレスを入力してください"
	if not password:
		error["password"] = "パスワードを入力してください"
	if not (password == password_conf):
		error["password"] = "パスワードが一致しません"
		
	if not user_name:
		error["user_name"] = "氏名を入力してください"
	if not home_address:
		error["home_address"] = "住所を入力してください"
	if not gender:
		error["gender"] = "性別を選択してください"
	if not birth_date:
		error["birth_date"] = "生年月日を選択してください"
	if not credit_id:
		credit_id = None
	if credit_id.isdigit():
		error["credit_id"] = "クレジットカードIDには数字のみを入力してください"
		

	#一つも入力漏れがない時
	if len(error) == 0:
		if gender == "男":
			gender = 1
		else:
			gender = 0
		# ユーザ登録
		try:
			sql = f"insert into `Account`(`Account_id`,`Mail_address`,`Password`,`User_name`,`Home_address`,`Gender`,`Birth_date`,`Credit_id`) values(null,'{mail_address}','{password}','{user_name}','{home_address}','{gender}','{birth_date}','{credit_id}')"
			connection_MySQL(sql,"w","hotel")
		except:
			print("Location:http://192.168.42.128\n")
		print("Location:http://192.168.42.128\n")
	else:
		with open("../html/adduser.html",mode="r",encoding="utf-8") as html:
			print("Content-Type: text/html\n")
			print(html.read())