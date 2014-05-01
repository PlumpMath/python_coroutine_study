# coding:utf-8

# recvcount.py
#
# Example of a co-routine

import time

def recv_count():
    try:
        while True:
            n = (yield)
            print "T-minus", n
    except GeneratorExit:
        print "Finished!"

r = recv_count()
r.next()
for i in range(5,0,-1):
    r.send(i)

r.close()

# rr = recv_count()

# import pdb; pdb.set_trace()
