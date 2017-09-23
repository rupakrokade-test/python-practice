def solution (A, K):
	i=0
	j=0
	counter=0
	# Write your code here
	for i in range(N):
		P_list=[]
		T_list=[]
		#counter=0
		for m in range(N):
			if A[i][m]=='P':
				P_list.append(m)
		for m in range(N):
			if A[i][m]=='T':
				T_list.append(m)
#		for j in range(N):
		print P_list
		print T_list
		for o in range(len(P_list)):
			delta=0
			while delta<K:
				delta=delta+1
				if T_list.count(P_list[o]-delta)!=0:
						counter=counter+1
				elif T_list.count(P_list[o]+delta)!=0:
						counter=counter+1
					

	print "----------"
	print counter
	print P_list
	print T_list
	print A


A=[['P', 'T', 'P'], ['T', 'P', 'T'], ['T', 'T', 'P']]
N=3
solution(A,1)