#!/usr/bin/python3 --
import cgi
import MySQLdb
import sensin

### main program ###
import crypt
error = {}
form = cgi.FieldStorage()

if form.list == []:
	#GET
	sensin.htmlpage("../html/login.html")
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
		error["test"] =sql
		result = sensin.connection_MySQL(sql,"r","hotel")

		if result:
			#login success
			account_id = result[0]
			session_key = sensin.get_random_str(64)
			sql = f"insert into Session (`Session_id`, Session_key, `Account_id`) values ('null','{session_key}',{account_id})"
			sensin.connection_MySQL(sql,"w","hotel")
			print("Location:./login_success.cgi\n")
		else:
			#login failed
			error["password"] = "メールまたはパスワードが一致しません"
			sensin.htmlpage("../html/login.html",error=error)
	else:
		#form error
		sensin.htmlpage("../html/login.html",error=error)




