import random
board=[]
j=0
k=1
for i in range(10):
	arr=[]
	for j in range(10):	
		if(i%2==0):
			arr.append(k)
		else :
			arr.insert(0,k)
		k+=1

	board.append(arr)		


for i in range(9,-1,-1):
	print(board[i])

ladder={2:38,4:14,9:31,33:85,52:88,80:99}
snake={56:15,62:57,92:53,51:11,98:8}
print(ladder)
print(snake)


a=1
b=1
turn= 0

while(1):
	flag=0
	if(turn==1):
		print("b's turn")
		input("roll enter 1\n")
	else:
		print("a's turn")
		input("roll enter 1\n")	
	dice=random.randint(1,6)
	print(dice)
	if(turn==0):
		if(a+dice<=100):
			a+=dice
			if(a  in ladder):
				a=ladder[a]
			if(a in snake):
				a=snake[a]
			if(a==100):
				flag=1
				break
	else:					
		if(b+dice<=100):
			b+=dice
			if(b in ladder):
				b=ladder[b]
			if(b in snake):
				b=snake[b]
			if(b==100):
				flag=2
				break		
	turn^=1		
	print(a,"a")
	print(b,"b")
print("winner id")	
if(flag==1):
	print("dee")
elif(flag==2):
	print("dhilu")		