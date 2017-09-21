def draw(l):
	print "\n----- ----- ------"
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
							break
						else:
							print "You cannot overwrite a previous move"
							continue
					else:
						print "Please enter a number between 1 to 9"		
		draw(l)

	print l

l=range(1,10)
#l[3]='X'
#l[4]='X'
#l[5]='X'
draw(l)
start(l)

