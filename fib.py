import argparse

def fib(n):
	a, b = 0, 1
	for i in range(n):
		a, b = b, a+b
	return a

def Main():
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-v", "--verbose", action="store_true")
	group.add_argument("-q", "--quiet", action="store_true")	
	parser.add_argument("num", help="the fibonacci number you wish to calculate", type=int)
	parser.add_argument("-o", "--output", help="Output result to a text file.", action="store_true")
	
	args = parser.parse_args()
	
	result = fib(args.num)
	
	if args.verbose:
		print("The "+str(args.num)+"th fib number : "+str(result))
	elif args.quiet:
		print(str(result))
	else:
		print("Fibonacci ("+str(args.num)+"): "+str(result))
		
	if args.output:
		f = open("fibonacci.txt", "a")
		f.write("The "+str(args.num)+"th fib number : "+str(result)+'\n')
		f.close()

if  __name__ == '__main__':
	Main()