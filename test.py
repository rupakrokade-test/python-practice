"""a=[1,2,3]
b=[1,3,4]

for i in b:
	if a.count(i)==1:
		print True
"""
l=[1,'X','X',4]
mark='X'
out=[]

def player(l,mark):
	for i in range(len(l)-1):
		if l[i]==mark:
			out.append(i)
	return out


print player(l,mark)