#lst=raw_input("Enter a list of numbers: ")

def less(lst):

	lst2=[]
	end=len(lst)
	for i in range(end-1):
		if lst[i]<10:
			lst2.append(lst[i])
	return lst2

lst=[1,4,5,88,66,55,3,2]
print less(lst)