#-*-coding:utf-8-*-

s = "����"
print type(s)	#�鿴s���ַ�����
print s

s.decode('utf8', "ignore")	#����utf8��Ĭ�ϵı��뷽ʽ�� unicode
s.decode('gbk', "ignore")		#����utf8,�����������쳣�ı��룬����ʾ��Ч���ı���
s.decode('gbk', "replace")

print type(s)
print s

#s.encode('gb2312',"ignore")	##����Ϊutf8
print type(s)
print s