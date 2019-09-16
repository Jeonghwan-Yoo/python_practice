while True:
	dan=int(input("what number you wanna see multiple:"))
	if dan==0:
		print('Good-Bye')
		break
	if dan<2 or dan>9:
		print('only 2~9')
		continue
		
	for i in range(1,9):
		print('{}*{}={}'.format(dan,i,dan*i))