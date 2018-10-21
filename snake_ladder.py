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

ladder={2:38,4:14,9:31,33:85,52:88,80:99} #using dictionary to create a ladder (start point to end point)
snake={56:15,62:57,92:53,51:11,98:8} # use dictionary to create a snake (start point end point(start point shoud be high for snake))
print(ladder)
print(snake)


a=1  #first player
b=1 #second player
turn= 0 #starts at player 1 and doing xor afer each iteration.
flag=0
while(1):
	 #kept this to decide the winner.
	if(turn==1):
		print("b's turn")
		input("roll enter 1\n") # this is not necessary but have added this to make player aware that it is their turn.
	else:
		print("a's turn")
		input("roll enter 1\n")	# this is not necessary but have added this to make player aware that it is their turn.
	dice=random.randint(1,6) # this gives number on dice.
	print(dice)
	if(turn==0):   #checks the condition for player 1
		if(a+dice<=100):
			a+=dice
			if(a  in ladder):
				a=ladder[a]
			if(a in snake):
				a=snake[a]
			if(a==100):
				flag=1
				break
	else:				 #checks the condition for player 2.	
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
	print(a,"a") #after every player prints player 1 and player 2 result
	print(b,"b")
print("winner is ", end="")	#final winner of the game.
if(flag==1):
	print("a")
elif(flag==2):
	print("b")		