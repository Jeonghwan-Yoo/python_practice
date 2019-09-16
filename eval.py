while True:
	expr=input("equation[exit=0]:")
	if expr=='0':
		break
	print("=>",expr,'=',eval(expr))
print("Good-Bye")