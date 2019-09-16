a=[1,2,3]
try:
	#print('haha')
	print(a.__next__())
except ZeroDivisionError:
	print('it can\'t be divided by 0')
except IndexError:
	print('out of the index')
except TypeError:
	print('That\'s not fitted in Type')
except:
	print('undefined error')
	
else:
	print('good')
finally:
	print('necessarily executed')