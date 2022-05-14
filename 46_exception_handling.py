#try except finally 
def function():
	pass
try : 
	a = int(input("Enter a Value : "))
	b = int(input("Enter a Value : "))
	c = a/b 
	print("{}/{}={}".format(a,b,c))

except ZeroDivisionError :
	print("Denominator can't be zero")

except ValueError : 
	print("Please Provide a Integer value only")





