#coding=utf-8

import re
import urllib
import time

datafile = open("Olddatafile.txt","wb+")

def getHtml(url):
		page = urllib.urlopen(url)
		html = page.read()
		return html

def getMsg(html):		
		
		head = "<table"
		tail = "</table>"
		fang = "<tr><td>"
		i = 0
		ph = -1
		pj = -1
		pb = -1
		pe = -1
		
		ph = html.find(head)
		pj = html.find(tail, ph + 1)
		table = html[ph+237 : pj]
		temp = table

		while (i < 20):
				pb = temp.find(fang)
				pe = temp.find(fang, pb + 4)
				print temp[pb : pe]
				datafile.write(temp[pb : pe]+"\n");				
				temp = temp[pe-1:]
				i += 1

j= 10
while (j <= 110 ):
		links = "http://anju.szhome.com/ajpm/" + str(j) + "-0-0-0-1-0/"
		print links
		html = getHtml(links)
		getMsg(html)
		
		j += 1
		time.sleep(3)

datafile.close()
                                                                                                                