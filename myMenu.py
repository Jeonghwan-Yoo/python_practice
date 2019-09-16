import sys
def fun1():
	print('=>insert function\n')

def fun2():
	print('=>delete function\n')
	
def fun3():
	print('=>select function\n')
	
def fun4():
	print('=>update function\n')
	
while True:
	print('1. insert')
	print('2. delete')
	print('3. select')
	print('4. update')
	print('0. exit')
	num=int(input('choice:'))
	if num==0:
		print('exit')
		sys.exit()
	elif num==1:
		fun1()
	elif num==2:
		fun2()
	elif num==3:
		fun3()
	elif num==4:
		fun4()
	else:
		print('{} no available'.format(num))
	