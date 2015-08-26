def divide(x, y):
	try:
		result = x / y
	except ZeroDivisionError,e:
		print "Division by zero! " + str(e)
	except TypeError:
	    divide(int(x), int(y))
	else:
		print "result is " + str(result)
	finally:
		print "Excuting finally clause"