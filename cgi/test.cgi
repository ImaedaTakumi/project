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
error = {}
form = cgi.FieldStorage()
cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE',''))


if form.list == []:
	#GET
	htmlText='''
	<!DOCTYPE html>
	<html lang="ja">
	<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<title>login</title>
	</head>
	<body>
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
	class CookieSession:
		"クッキーを使ったセッションのクラス"
		
		SESSION_ID = "CookieSessionId"
		# セッションデータの保存先を指定 os.path.dirname()でパスのディレクトリ名を取得
		SESSION_DIR = os.path.dirname(os.path.abspath(__file__)) + "/SESSION"
	
		def __init__(self):
			# セッションデータの保存パスを確認
			if not os.path.exists(self.SESSION_DIR):
				os.mkdir(self.SESSION_DIR)
	
			# クッキーからセッションIDを得る
			rc = os.environ.get("HTTP_COOKIE","")
			self.cookie = cookies.SimpleCookie(rc)
			if self.SESSION_ID in self.cookie:
				self.sid = self.cookie[self.SESSION_ID].value
			else:
				# 初回の訪問ならセッションIDを生成する
				self.sid = self.gen_sid()
	
			# 保存してあるデータを読み出す
			self.modified = False
			self.values = {}
			path = self.SESSION_DIR + "/" + self.sid
			if os.path.exists(path):
				with open(path,"r",encoding="utf-8") as f:
					a_json = f.read()
					# JSON形式のデータを復元
					self.values = json.loads(a_json)
	
		def gen_sid(self):
			"""セッションIDを生成する"""
			token = ":#sa$2jAiN"
			now = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
			rnd = random.randint(0,100000)
			key = (token + now + str(rnd)).encode("utf-8")
			sid = hashlib.sha256(key).hexdigest()
			return sid
	
		def output(self):
			"""クッキーヘッダを書き出す"""
			self.cookie[self.SESSION_ID] = self.sid
			self.save_data()
			return self.cookie.output()
	
		def save_data(self):
			"""セッションデータをファイルに書き出す"""
			if not self.modified:
				return
			path = self.SESSION_DIR + "/" + self.sid
			# JSON形式に変換して保存
			a_json = json.dumps(self.values)
			with open(path,"w",encoding="utf-8") as f:
				f.write(a_json)
	
		# 添字アクセスのための特殊メソッドの定義
		def __getitem__(self,key):
			return self.values[key]
	
		def __setitem__(self,key,value):
			self.modified = True
			self.values[key] = value
	
		def __contains__(self,key):
			return key in self.values
	
		def clear(self):
			self.values = {}
	
	cgitb.enable()
	# 実行テスト(訪問カウンタの例)
	ck = CookieSession()
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


