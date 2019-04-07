from random import shuffle
def  getAltrnte(A):
	n=len(A)
	i=0
	j=n-1
	c=[]
	while i<n//2:
		c.append(a[i])
		#print(a[i],end=" ")
		i=i+1
		#print(a[j],end=" ")
		c.append(a[j])
		j=j-1
	# print("")
	# print(n,len(c))
	return c

a=[x for x in range(1,7)]
shuffle(a)

print("A: "+str(a))
a.sort(reverse=True)
print("Sorted A: "+str(a))
print("AlternateSorted A: "+str(getAltrnte(a)))


"""
Step:1>Sorting of A
Step:2>
Keep i at start 
and j at the end of A
Step:3>
n=(size of A)-1
Loopng i from 0 to n/2
	printing a[i] and a[j] 
	successively as well as 
	incremnting i nd decremnting j respectively
"""
