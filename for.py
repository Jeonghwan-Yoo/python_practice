print('*numbering*')

print('[{:d}]'.format(777))
print('[{:10}]'.format(777))
print('[{:>10}]'.format(777))
print('[{:<10}]'.format(777))
print('[{:^10}]'.format(777))

print('*character*')

print('[{:}]'.format('!'))
print('[{:10}]'.format('!'))
print('[{:>10}]'.format('!'))
print('[{:<10}]'.format('!'))
print('[{:^10}]'.format('!'))

print('*string*')

print('[{:}]'.format('python'))
print('[{:20}]'.format('python'))
print('[{:>20}]'.format('python'))
print('[{:<20}]'.format('python'))
print('[{:^20}]'.format('python'))

print('1.--------\n')
for i in range(5):
	print('*'*(i+1))

print('\n2.--------\n')
for i in range(5):
	print('{:<5}'.format('*'*(i+1)))
	
print('\n3.-----------\n')
for i in range(5):
	print('{:>5}'.format('*'*(i+1)))
	
print('\n4.-----------\n')
for i in range(5,0,-1):
	print('{:>5}'.format('*'*(i-1)))
	
print('\n5.-----------\n')
for i in range(5,0,-1):
	print('{:<5}'.format('*'*(i-1)))
	
print('\n6.-----------\n')
for i in range(1,11,2):
	print('{:^10}'.format('*'*i))
for i in range(9,0,-2):
	print('{:^10}'.format('*'*i))
	
print('\n7.-----------\n')
for i in range(9,0,-2):
	print('{:^10}'.format('*'*i))
for i in range(3,11,2):
	print('{:^10}'.format('*'*i))
