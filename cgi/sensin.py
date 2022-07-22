import cgi
import MySQLdb
import random, string
from collections import defaultdict
from datetime import datetime
import os ,json
from http import cookies
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

def htmlpage(page,text=[""],error={}):
	with open(page,mode="r",encoding="utf-8") as html:
		print("Content-Type: text/html\n")
		data = defaultdict(lambda: str())
		for i,j in error.items():
			data[i] = j
		print(html.read().format(text,data))

def read_cookie():
	cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE',''))
	try:
		session_key = cookie["session_key"].value
	except KeyError:
		session_key = ""
		
	sql = f"select `Mail_address`, `Account_id` from Account natural inner join Session where Session_key = '{session_key}'"
	cookielogin = connection_MySQL(sql,"r","hotel")
	return cookielogin
		

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