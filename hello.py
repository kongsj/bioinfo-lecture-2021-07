#! /usr/bin/python

import sys

print(sys.argv) #sys.argv는 리스트list
sys.exit() #여기까지만 실행



name = sys.argv[1]      
name2 = sys.argv[2]

print(f"Hello {name}")
print(f"Hello {name2}")

