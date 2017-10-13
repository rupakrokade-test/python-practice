import sys

def draw(l):
	print "\n----- ----- -----"
	for k in range(3):
		for i in range(3):
			if k==0:
				i=i
			elif k==1:
				i=i+3
			elif k==2:
				i=i+6
			#print " --- ",
			print("| %s |")% l[i],
		print "\n----- ----- -----"




def player(l,mark):
	out=[]

	for i in range(len(l)):
		if l[i]==mark:
			out.append(i+1)
	return out


def winner(mark,vec):
	vec=player(vec,mark)
	#print vec
	play_set=set(vec)
	#print play_set
	win_list=[{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,7,5}]

	if len(vec)>2:
		for itr in win_list:
			if itr&play_set==itr:
				return True
				break



def start(l):
	stack=[]
	for i in range(9):
		if i%2!=0:
			while True:
				data=raw_input("Player 2's turn to choose a position to put O: ")
				try:
					data=int(data)
				except:
					print "Please put a valid number between 1 to 9"
					continue
				else:
					if (data>0) & (data<10):
						if stack.count(data)==0:
							stack.append(data)
							l[data-1]='O'
							#print winner('X',l)
							if winner('O',l)==True:
								draw(l)
								sys.exit("Player 2 with 'O'  wins the Game !!!")
							break
						else:
							print "You cannot overwrite a previous move"
							continue
					else:
						print "Please enter a number between 1 to 9"
		else:
			while True:
				data=raw_input("Player 1's turn to choose a position to put X: ")
				try:
					data=int(data)
				except:
					print "Please put a valid number between 1 to 9"
				else:
					if (data>0) & (data<10):
						if stack.count(data)==0:
							stack.append(data)
							l[data-1]='X'
							#print winner('X',l)
							if winner('X',l)==True:
								draw(l)
								sys.exit("Player 1 with 'X' wins the Game !!!")
							break
						else:
							print "You cannot overwrite a previous move"
							continue
					else:
						print "Please enter a number between 1 to 9"		
		draw(l)
		#print l
	print "Too bad... Its a DRAW"
l=range(1,10)
draw(l)
start(l)
