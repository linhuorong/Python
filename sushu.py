#!/usr/bin/python
# -*- coding: utf-8 -*-

i = 2
while(i < 100):
	j = 2
	while(j <= (i/j)):
		if not(i%j): break
		j = j + 1
	if (j > i/j) : print i, " ÊÇËØÊý"
	i = i + 1

for letter in 'Python':
		if letter == 'h':
			break
		print 'Current Letter :',letter

var = 10
while var > 0:
	print 'Current variable value :', var
	var = var - 1
	if var == 5:
		break



print "Good bye!"