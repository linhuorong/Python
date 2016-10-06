#!/usr/bin/python
#-*- coding:UTF-8 -*-

import time

localtion = time.localtime(time.time())
print "本地时间：", localtion

time2 = time.asctime( time.localtime(time.time()))

print "time2: ", time2

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

a = "Sun Oct 03 23:18:00 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))


import calendar

cal = calendar.month(2016, 10)
print "calendar of  2016.10 :"
print cal;
