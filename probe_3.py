
def main(args):
    
	data = "AAABXGHJAXGHJHBBXHJKIAXFDBAXDFRBXRERGTHAXBX"
	print('Data =',data)
	l = list(data)
	cnt = 0
    
	for i in range(len(l)):
		
		if l[i]=='B' and l[i+1]=='X':
			flagInit = True
			
		if l[i]=='A' and l[i+1]=='X' and flagInit==True:
			flagInit = False
			cnt = cnt+1
	print(' ')
	print('Packets =',cnt)
    
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
