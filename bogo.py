from random import shuffle

def isSorted(A):
	for i in range(len(A)-1):
		if a[i]>a[i+1]:
			return False
	return True
def bogoNow(A):
	print("A is Bogging.......")
	while not isSorted(A):
		shuffle(A)
		#print("Suffffffling....")
				
	return A


n=6
a=[x for x in range(1,n)]
shuffle(a)
print("A: "+str(a))
print("A after getting Bogged: "+str(bogoNow(a)))


"""
Worst case complexity is O(infinity)
as number of n increases e.g:n=11
output time cannot be predicted
"""

