a=[1,2,3]
try:
	a[5]=6
except (ZeroDivisionError,IndexError,TypeError):
	print('ZeroDivisionError,IndexError or TypeError')
except:
	print('undefined error')
	
else:
	print('good')
finally:
	print('necessarily executed')