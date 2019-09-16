while True:
	score=int(input("score:"))
	if score==0:
		print('Good-Bye')
		break
	if score>=90:
		print(score,"su")
	elif score>=80:
		print(score,"u")
	elif score>=70:
		print(score,"mi")
	elif score>=60:
		print(score,"yang")
	else:
		print(score,"ga")