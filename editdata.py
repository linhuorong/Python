#coding=utf-8

import time

tablefile = open("J:\\Python\\EditData\\tablefile_edit.txt","rb")
editfile  = open("J:\\Python\\EditData\\editfile.txt","wb")

j= 1
outrec = " \n"


def findli(ulr):
	global outrec
	lib = "<li>"
	lie = "</li>"
	li_flag = False
	libf = ulr.find(lib)
	lief = ulr.find(lie, libf+1)
	
	while( libf >= 0 and lief >= 0):
		li_flag = True
																
		outrec = outrec + ulr[libf + 4 : lief] + "\t"
		
		ulr = ulr[lief+4 : ]
		libf = ulr.find(lib)
		lief = ulr.find(lie, libf+1)
	
	else:
		if (li_flag == False):
			outrec = outrec + ulr + "\t"
			

def findul(tdr):
	global outrec
	ulb = "<ul>"
	ule = "</ul>"
	ul_flag = False
	ulbf = tdr.find(ulb)
	ulef = tdr.find(ule, ulbf + 1)
										
	while( ulbf >= 0 and ulef >= 0):
		ul_flag = True
		print "ul part: ", tdr
		
		findli(tdr[ulbf+4 : ulef])
		
		tdr = tdr[ulef+4 : ]
		ulbf = tdr.find(ulb)
		ulef = tdr.find(ule, ulbf + 1)
	
	else:
		if (ul_flag == False):
			outrec = outrec + tdr + "\t"


def findtd(record):
	tdb = "<td"
	tde = "</td>"
	td_flag = False
	tdbf = record.find(tdb)
	tdef = record.find(tde, tdbf + 1)
									
	while( tdbf >= 0 and tdef >= 0):
		td_flag = True
		print "td part: ", record
		
		findul(record[tdbf+4 : tdef])
		
		record = record[tdef+4 : ]
		tdbf = record.find(tdb)
		tdef = record.find(tde, tdbf + 1)
	
	else:
		if (td_flag == False):
			print "the record has no td item! "


def findtr(line):
	global outrec
	trtdb = "<tr><td>"
	trtde = "</td></tr>"			
	trtd_flag = False
	trbf = line.find(trtdb)
	tref = line.find(trtde, trbf + 1)
									
	while( trbf >= 0 and tref >= 0):
		trtd_flag = True
		print "line part: ", line
		
		findtd(line[trbf+4 : tref+5])
		
		line = line[tref+8 : ]
		trbf = line.find(trtdb)
		tref = line.find(trtde, trbf + 1)
		
		editfile.writelines(outrec)	
		outrec = " \n"
	
	else:
		if (trtd_flag == False):
			print "the line has no trtd item! "
					



line = tablefile.readline()

while ( line and j <= 2561 ):				#max=2561

		try:
			
			print "Begin process record " + str(j)
			
			findtr(line)

		except IOError:
			print "IOError occure!"

		j += 1
		line = tablefile.next()

		
tablefile.close()
editfile.close()