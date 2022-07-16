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

def htmlpage(page,text=[""],error=[""]):
	with open(page,mode="r",encoding="utf-8") as html:
		print("Content-Type: text/html\n")
		print(html.read().format(text,error))