def plus(a,b):
	return a+b
def minus(a,b):
	return a-b
def multi(a,b):
	return a*b
def divi(a,b):
	return a//b

while(True):
	print('simple calculator')
	print('exit:0')
	print('***********')
	
	number1=int(input('first number:'))
	if(number1==0):
		print('Good-Bye')
		break
	oper=str(input('+,-,*,/:'))
	
	number2=int(input('second number:'))
	
	if(oper=='+'):
		res=plus(number1,number2)
	elif(oper=='-'):
		res=minus(number1,number2)
	elif(oper=='*'):
		res=multi(number1,number2)
	elif(oper=='/'):
		res=divi(number1,number2)
	else:
		print('{} no operation'.format(oper))
		
	print('result:{} {} {} = {}'.format(number1,oper,number2,res))