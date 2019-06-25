#!/usr/bin/python36

#install google library for this program via 'pip install google'

import webbrowser
from googlesearch import search
file=open('url.txt','a+')
data=input("Enter data to be searched \t")
searched=search(data,stop=10)
for url in searched:
	file.write(url+"\n\n")
	webbrowser.open(url)
