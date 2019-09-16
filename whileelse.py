import sys

while True:
	city=str(input('which city is the popular:'))
	
	while city=="seoul":
		print('{} yes'.format(city))
		sys.exit()
	else:
		print('{} no. Do again'.format(city))
		continue