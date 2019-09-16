for i in range(10):
	print(i,"==>python")
	
for i in range(10):
	if i==3:
		continue
	print(i,"==>python")
	
for i in range(10):
	if i==3:
		break
	print(i,"==>python")
	
while True:
	score=int(input("score[exit:-1]:"))
	if score==-1:
		print("Good-Bye")
		break
	if not 0<=score<=100:
		print("only -0~100")
		continue
	print("=>",score,"is score.",end="\n\n")