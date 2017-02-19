lists = list(raw_input("Enter a comma seperated Vector without brackets: ").split(","))
new_list=list()
#print(lists)

for i in lists:
  if int(i)<5:
    new_list.append(i)

print(new_list)

index = int(raw_input("Input the index of the number you want: "))
print(new_list[index-1])
