# coding:utf-8
# 利用 Generator 實現 Coroutine 來切割 Method 內的工作。
# 用 Generator 製作 Coroutine 可以自由的在副程式內用 yield 調用時機控制執行流程。
# 但是遇到類似 sleep 的 I/O 還是會卡住。

def domsomething():
	# 第一部分
	print 1
	print 2
	yield
	# 第二部分
	print 3
	print 4
	print 5
	# 第三部分
	yield
	print 6
	print 7

work = domsomething()

while True:
	try:
		print 'Work clip...'
		work.next() 
	except:
		print 'my work end!'
		break

# import pdb; pdb.set_trace()
