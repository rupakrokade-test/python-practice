def palindrome(a):
    valid=len(a)*1.0
    if valid%2==0:
    	print "The given string is not a palindrome"
    else:
    	ind=int(round(valid/2.0))
    	data1=a[0:ind-1]
    	data2=a[len(a):ind-1:-1]
    	if data1==data2:
    		print "Given string is palindrome"
    	else:
    		print "Given string is not a palindrome"

palindrome("madam")