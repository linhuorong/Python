#coding=utf-8

import urllib
import time

j= 1
while (j <= 2561 ):				#max=2561
		links = "http://anju.szhome.com/ajpm/" + str(j) + "-0-0-0-1-0/"
		print links

		filename = "J:\\Python\\data\\data_" + str(j) + ".html"
		print filename
		
		try:
			testfile = open(filename, "r")
			testfile.close()
		except IOError:
			try:
				print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
				urllib.urlretrieve(links,filename)
			except IOError:
				print "data_" + str(j) + ".html download fail!"
			else:
				print "data_" + str(j) + ".html download done!"
				
		j += 1
		#		time.sleep(1)