#coding=utf-8

import urllib
import time

j = 93
#while (j <= 100 ):				#max=2561
links = "http://anju.szhome.com/ajpm/" + str(j) + "-0-0-0-1-0/"

filename = "J:\\Python\\data\\data_" + str(j) + ".html"
		
testfile = open(filename, "wb")

urllib.urlretrieve(links,filename)
		
testfile.close()