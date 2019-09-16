import os

while True:
	print('menu')
	print('*****')
	print('1.notepad')
	print('2.calculator')
	print('3.cmd')
	print('0.exit')
	menu=int(input('choose:'))
	if menu==0:
		print('Good-Bye')
		break
	if menu==1:
		os.system('notepad')
	elif menu==2:
		os.system('calc')
	elif menu==3:
		os.system('cmd')
	else:
		continue