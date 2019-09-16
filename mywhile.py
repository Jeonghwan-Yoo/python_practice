while True:

	dan=int(input('multiple:'))

	if dan==0:
		print('{}. exit'.format(dan))
		break
	if dan<2 or dan>9:
		print('{} is not. Please rewrite'.format(dan))
		continue
	
	print('{} output'.format(dan))
	
	i=1
	while i<=9:
		print('{}*{}={:2d}'.format(dan,i,dan*i))
		i=i+1
		
		
	