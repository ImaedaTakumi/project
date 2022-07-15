#!/usr/bin/python3 --
import cgi

with open("../html/login_success.html",mode="r",encoding="utf-8") as html:
		print("Content-Type: text/html\n")
		print(html.read())