# coding: utf-8

import signal, urllib2
import time

def process():
	for i in xrange(0,10):
		print 'do something' + str(i)
		urllib2.urlopen('http://blue5069.idv.tw')  # make a I/O operation
		yield i

# 建立 Coroutine Task, 此時不會真的執行內容
main = process()

while True:
	try:
		main.next()
		print 'return to main...'
	except:
		break

import pdb; pdb.set_trace()
