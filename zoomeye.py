# -*- coding: utf-8 -*-
#-*- by:Lee -*-
#-*- date:2017-3-28 -*-
import requests
import json
import time
import re
import threading
def get_url(url):
	data = {'username': "Your Username",'password': "Your Password"}		#this is zoomeye login
	data_encoded = json.dumps(data)
	results=open("result1.txt","a+")
	urls='https://api.zoomeye.org/user/login'	
	a=requests.post(urls,data_encoded)
	JWT=a.text
	token="JWT"+" "+JWT[18:-2]
	#print(token)
	header={"Authorization":token}
	X=requests.get(url,headers=header)
	html=X.text
	result=[]
	x=json.loads(html)
	for w in x['matches']:
		for a,b in w.items():
			if a=="webapp":
				#print b
				for c in b:
					for d,f in c.items():
						if d=="url":
							#print f
							result.append(f)
							results.write(f+"\n")
							

for i in range(1,1000):
	url='https://api.zoomeye.org/web/search?query=phpmyadmin+country%3AFR&page='+str(i)
	get_url(url)
	print "GET URL FOR:"+url+" IS OK!"
	
					

'''
city
country
isp
asn
subdivisions
location
organization
aso
continent
hostname
service
os
app
extrainfo
version
device
banner
port
'''
'''
language
ip
waf
component
system
db
framework
webapp
server
domains
language
ip
waf
component
system
db
framework
webapp
server
domains
'''
	