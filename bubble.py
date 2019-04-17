import random
def bubbly(A):
	n=len(A)
	for i in range(0,n):
#		print(A[i],end=" ")
		for j in range(0,i):
			if a[i]<a[j]:
				a[i],a[j]=a[j],a[i]
	return A
a=random.sample(range(1,10),4)
print(a)
print("")
print(bubbly(a))







