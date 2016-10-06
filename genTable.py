#coding=utf-8

import time

tablefile = open("J:\\Python\\EditData\\tablefile_test.txt","wb")

j= 1
error = 0

while (j <= 2561 ):				#max=2561

		filename = "J:\\Python\\data\\data_" + str(j) + ".html"
		
		try:
			testfile = open(filename, "rb")
			filedata = testfile.read()
			
			head = '<table'
			tail = "</table>"
			
			ph = filedata.find(head)
			pj = filedata.find(tail, ph + 1)
			
			if (ph > 0 and pj > 0):
				tablefile.write(filedata[ph : pj+8]+"\n");
			else:
				print "data_" + str(j) + ".html don't has any table!"
				error += 1
			
			testfile.close()
		except IOError:
			print "data_" + str(j) + ".html open fail!"
			error += 1

		j += 1

print " total error: ", error
