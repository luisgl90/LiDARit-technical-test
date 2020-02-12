import math

def main(args):
	
	d = 100 # meters
	
	d_arr = [] # distances array
	
	for ang in range(-15,16,2):
		print(ang)
		valDist = d/math.cos(ang*math.pi/180)
		d_arr.append(format(valDist,'.3f'))
		
		
	print(d_arr)
		
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
