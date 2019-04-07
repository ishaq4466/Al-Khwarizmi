def merge(A,B):
	n=len(A)
	m=len(B)
	i=j=0
	c=[]
	while i<n and j<m:
		if(a[i]<b[j]):
		#	print(a[i],end=" ")
			c.append(a[i])
			i=i+1
		else:
		#	print(b[j],end=" ")
			c.append(b[j])
			j=j+1
	while i<n:
		c.append(a[i])
		#print(a[i],end=" ")
		i=i+1
	while j<m:
		c.append(b[j])
		#print(b[j],end=" ")
		j=j+1
	#print("")
	#print("Merged:"+str(c))
	return c
#a=input().split(" ")
#a=[1,3,5,6]
#b=[2,13,18,22,25]
a=[int(x) for x in input().split(" ")]
b=[int(x) for x in input().split(" ")]
print("A:"+str(a))
print("B:"+str(b))
print("Merged: "+str(merge(a,b)))