b=50000

def fun(x):
	b=x #local
	print("x= ",x,"b= ",b)
	
def fun2(x):
	print("x= ",x,"b= ",b)
	
fun(10)
fun2(500)

print("b= ",b)

b=99999

print("b= ",b)

def fun4(x):
	global b #global
	b=x
	print("x= ",x,"b= ",b)

fun(100)
fun2(500)
fun4(700)

print("b= ",b)

b=99999
print("b= ",b)

fun4(33)
print("b= ",b)