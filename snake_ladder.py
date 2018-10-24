#Made a snake and ladder game, using tkinter python GUI library, green lines represent snakes, yellow lines represent ladder
from tkinter import Tk, Canvas, Frame, Label, Button, BOTH, TOP, BOTTOM
import random
from functools import partial

MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 10  # Width and height of the whole board
a=1 #for player 1
b=1 #for player 2
turn=0
def make_grid(root,canvas):
	for i in range(11):
		color = "black"
		x0 = MARGIN + i * SIDE
		y0 = MARGIN
		x1 = MARGIN + i * SIDE
		y1 = HEIGHT - MARGIN
		# print(x0," ",y0," ",x1," ",y1)
		canvas.create_line(x0, y0, x1, y1, fill=color)
		x0 = MARGIN
		y0 = MARGIN + i * SIDE
		x1 = WIDTH - MARGIN
		y1 = MARGIN + i * SIDE
		# print(x0," ",y0," ",x1," ",y1)
		canvas.create_line(x0, y0, x1, y1, fill=color)

def draw_board(root, canvas,board):
	canvas.delete("numbers")
	for i in range(10):
		for j in range(10):
			answer=board[i][j] 
			if( (j+i)%2==0 ):
				color="blue"
			else:
				color="red"
			x=MARGIN+j*SIDE+SIDE//2
			y=MARGIN+i*SIDE+SIDE//2
				
			canvas.create_text(
				x,y,text=answer ,tags="numbers" , fill=color
				)

def create_ladder(root,canvas,ladder):
	color="yellow"
	for key, value in ladder.items():
		r=(100-key)//10
		c=(key+9)%10
		if( r%2==0):
			c=9-c
		x0=MARGIN+r*SIDE+SIDE//2
		y0=MARGIN+c*SIDE+SIDE//2
		
		r=(100-value)//10
		c=(value+9)%10
		if(r%2==0):
			c=9-c
		x1=MARGIN+r*SIDE+SIDE//2
		y1=MARGIN+c*SIDE+SIDE//2

		canvas.create_line(y1, x1, y0, x0 ,fill=color,width="10")

def draw_snake(root,canvas,snake):
	color="green"
	for key, value in snake.items():
		r=(100-key)//10
		c=(key+9)%10
		if( r%2==0):
			c=9-c
		x0=MARGIN+r*SIDE+SIDE//2
		y0=MARGIN+c*SIDE+SIDE//2
		
		r=(100-value)//10
		c=(value+9)%10
		if(r%2==0):
			c=9-c
		x1=MARGIN+r*SIDE+SIDE//2
		y1=MARGIN+c*SIDE+SIDE//2

		canvas.create_line(y1, x1, y0, x0 ,fill=color,width="10", dash=(6,5, 2,4))

def draw_victory(root,canvas,color):
        # create a oval (which will be a circle)
        x0 = y0 = MARGIN + SIDE * 2
        x1 = y1 = MARGIN + SIDE * 7
        canvas.create_oval(
            x0, y0, x1, y1,
            tags="victory", fill=color, outline=color
        )
        # create text
        x = y = MARGIN + 4 * SIDE + SIDE / 2
        canvas.create_text(
            x, y,
            text="You win!", tags="winner",
            fill="white", font=("Arial", 32)
        )

def play_game(root):
	#starts at player 1 and doing xor afer each iteration.
	global a
	global b
	global turn
	flag=0
	# turn=0
	#kept this to decide the winner.
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
	else:				 #checks the condition for player 2.	
		if(b+dice<=100):
			b+=dice
			if(b in ladder):
				b=ladder[b]
			if(b in snake):
				b=snake[b]
			if(b==100):
				flag=2
			move_the_pointer()			
	print(a,"a") #after every player prints player 1 and player 2 result
	print(b,"b")
	#final winner of the game.
	if(flag==1):
		draw_victory(root,canvas,"orange")
		print("winner is a")
	elif(flag==2):
		draw_victory(root,canvas,"gray")
		print("winner is b")
	turn^=1		


root = Tk()
canvas = Canvas(root,width=WIDTH, height=HEIGHT)
canvas.pack(fill=BOTH,side=TOP)
Label= Label(root,text="Snake & Ladder")
Label.pack()
board=[] # contains numbers
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

	board.insert(0,arr)

ladder={2:38,4:14,9:31,33:85,52:88,80:99} #using dictionary to create a ladder (start point to end point)
snake={56:15,62:57,92:53,51:11,98:8} # use dictionary to create a snake (start point end point(start point shoud be high for snake))
make_grid(root,canvas)
draw_board(root,canvas,board) #fn to make board for snake and ladder
create_ladder(root, canvas,ladder) #function to make ladder
draw_snake(root,canvas,snake) # fn to make snakes
player1=partial(play_game,root)
button1=Button(root, text="Roll the dice!",command=player1) # this is not necessary but have added this to make player aware that it is their turn.
button1.pack()
QUIT= Button(root,text="Don't want to play? Click Game",fg="red", command=root.destroy) # when user wants to end the game.
QUIT.pack()
root.mainloop() 

	

