def miniMaxSum(arr):
	sum1=0
	sumList=[]
	if(specialCase(arr)):
		del arr[0]
		print(sum(arr),sum(arr))
		return
	for n in range(len(arr)):
		sum1=0
		exclude=arr[n]	
		for b in arr:
			if b==exclude:
				pass
			else:
				sum1+=b
		#		print(b,end="")	
		print("Sum of arr when %d excluded %d"%(exclude,sum1))
		sumList.append(sum1)
		#print("")
	print(sumList)
	print(min(sumList),max(sumList))

def specialCase(arr):
	x=arr[0]
	for a in arr:
		if(a!=x):
			return 0
	return 1


b=[x for x in range(5,11)]
#b=[5,5,5,5,5]

miniMaxSum(b)
#del b[0]
print(b)


"""
Getting the minimum and 
maximum sum of given array
e.g 
I/P:
arr=[5, 6, 7, 8, 9, 10]
O/P:
Sum of arr when 5 excluded 40<---maximum sum
Sum of arr when 6 excluded 39
Sum of arr when 7 excluded 38
Sum of arr when 8 excluded 37
Sum of arr when 9 excluded 36
Sum of arr when 10 excluded 35<--minimum sum
35 40

arr=[5,5,5,5]==>Special case
==================================================
Algo:
n=size of arr
sumlist=[]

Call specialCase
Loop from i=0 to i=n-1:
	exclude the arr[i] from arr
	initialize sum1=0
	Loop from j=0 to j=n-1:
		if arr[j] is excluded arr[i]
			pass
		else
			sum1+=arr[j]
		j<-j+1
	append sum1 to sumlist
	i<-i+1
Finally return max and min from sumlist

Algo for SpecialCase(when array contains all same values):
	remove arr[0]
	return min and max of arr
	and stop
"""

