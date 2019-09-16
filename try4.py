a=[1,2,3]
try:
	a[2]=4
except ZeroDivisionError:
	print('it can\'t be divided by 0')
except IndexError:
	print('out of the index')
except TypeError:
	print('That\'s not fitted in Type')
else:
	print('good')
	