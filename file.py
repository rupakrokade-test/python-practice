f=open("newfile.txt","a+")
f.write("some more added text\n")
f.close()

f=open("newfile.txt","r")
content=f.read()

print content