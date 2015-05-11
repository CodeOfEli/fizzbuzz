import sys

if len(sys.argv) >= 2:
	n = int(sys.argv[1])
else: 
	print "Please enter your request like this 'python fizzbuzz.py 15'"
	answer = raw_input("How many times would you like fizzbuzz to run?")
	n = int(answer)

print "Fizz buzz counting up to " + str(n) 

def fizzbuzz(x):
	#for x in range(1,x+1):
    	if x % 3 == 0 and x % 5 == 0:
        	print "Fizz Buzz \n"
    	elif x % 3 == 0:
        	print "Fizz \n"
    	elif x % 5 == 0:
        	print "Buzz \n"
    	else:
        	print "{} \n".format(x)

for n in range(1,n+1):
	fizzbuzz(n)





