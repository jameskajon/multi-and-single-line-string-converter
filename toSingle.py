#!/usr/bin/env python3
from sys import argv, exit

def toSingle():						# input to simgle of to multi with 's' or 'm'
	f = open('/Users/JimmyKajon/Desktop/NDT Work/Science/Astronomy/angular size/multi-line & single converter/input.txt', 'r+')
	lines = f.readlines()
	mystr = '[(startofnewline)]'.join([line.strip() for line in lines])
	f.seek(0)
	f.truncate()
	f.write(mystr)
	f.close()

if __name__ == '__main__':
	toSingle()