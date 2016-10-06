#coding=utf-8

import re
import urllib
datafile = open("datafile.txt","ab+")

def getHtml(url):
		page = urllib.urlopen(url)
		html = page.read()
		return html

def getMsg(html):
		
		head = 'tr class'
		tail = "width:400px"
		i = 0
		ph = -1
		html_tmp = html

		while (i < 15):
				ph = html_tmp.find(head)
				pj = html_tmp.find(tail, ph + 1)
				print "ph = ", ph
				print "pj = ", pj
				print html_tmp[ph : pj]
				datafile.write(html_tmp[ph : pj]+"\n");
				
				html_tmp = html_tmp[pj:]
				i += 1




#html = getHtml("http://bzflh.szjs.gov.cn/TylhW/lhmcAction.do?page=1&method=queryYgbLhmcInfo&waittype=1")
html = getHtml("http://123.207.12.157/getdata.html")

getMsg(html)

datafile.close()
                                                                                                                