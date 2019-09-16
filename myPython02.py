while True:
	print('where do you live in')
	print('seoul')
	print('busan')
	print('ulsan')
	print('incheon')
	print('daegu')
	print('gwangju')
	print('daejeon')
	print('exit:q')
	
	city=str(input("live in:"))
	if city=='q':
		print('Good-Bye')
		break
	
	if city=='seoul':
		print('hi', city)
	elif city=='busan':
		print('hi', city)
	elif city=='ulsan':
		print('hi', city)
	elif city=='incheon':
		print('hi', city)
	elif city=='daegu':
		print('hi', city)
	elif city=='gwangju':
		print('hi', city)
	elif city=='daejeon':
		print('hi', city)
	else:
		print('{} never heard of it the place sorry'.format(city))