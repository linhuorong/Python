#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Function:
�����������Windows�¿���Python���������Python�ű���
 
http://www.crifan.com/how_to_do_python_development_under_windows_environment
 
Author:     Crifan Li
Version:    2012-12-06
"""
  
import platform;
  
pythonVersion = platform.python_version();
uname = platform.uname();
  
print "Just for demo how to do python development under windows:";
print "Current python version info is %s"%(pythonVersion);
print "uname=",uname;
