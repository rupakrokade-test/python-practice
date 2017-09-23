def maximum(a):
  end = len(a)
  pk=0
  for i in range(end-1):
    if i==0:
      if a[i]>a[i+1]:
        pk=a[i]
    elif i!=end and a[i]>=a[i+1] and a[i]>=a[i-1]:
      pk=a[i]
    elif a[i]>=a[i-1]:
      pk=a[i]
  return pk

a=[1,7,2,7,4,3]
maximum(a)
