from sys import argv

def main(SorM):						# input to simgle of to multi with 's' or 'm'
	f = open('input.txt', 'r+')
	lines = f.readlines()
	if SorM == 's':
		mystr = '[(startofnewline)]'.join([line.strip() for line in lines])
	elif SorM == 'm' and len(lines) > 0:
		mystr = lines[0].replace('[(startofnewline)]', '\n')
	f.seek(0)
	f.truncate()
	f.write(mystr)
	f.close()

if __name__ == '__main__':
	main(argv[1])