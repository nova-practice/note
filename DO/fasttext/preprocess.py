#!/usr/bin/python
#-*- coding:utf-8 -*-
import re
import os

f = open('/data/data/文本分类语料库/交通214/41.TXT')
contents = f.read()
# print(contents.decode('gbk'))
string = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8"), "".decode("utf8"), contents.decode('gbk'))
print(string)

f.close()


filter=[".TXT", ".txt"]

def path(dirname):
	result = [];
	for maindir, subdir, filename_list in os.walk(dirname):
		for filename in filename_list:
			apath = os.path.join(maindir, filename)
			ext = os.path.splitext(apath)[1]

			if ext in filter:
				result.append(apath)
	return result


r = path('/data/data/文本分类语料库')

print(len(r))


print r