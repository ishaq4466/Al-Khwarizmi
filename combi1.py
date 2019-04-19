def genWithRep(A):
	size=len(A)
	#print(size)
	listOfList=[]
	small=[]
	count=0
	for i in range(0,size-1):
		for j in range(0,size-1):
			for k in range(0,size-1):
				small=[]
				small=[A[i],A[j],A[k]]
				#print(A[i],A[j],A[k])
				count=count+1
				#print(small)
				listOfList.append(small)
	#print(listOfList)
	#print("No of combi: %d"%(len(listOfList)))
	return listOfList

def genWithoutRep(A):
	size=len(A)
	#print(size)
	listOfList=[]
	small=[]
	count=0
	for i in range(0,size-2):
		for j in range(0,size-1):
			for k in range(0,size-3):
				small=[A[i],A[j],A[k]]
				#print(A[i],A[j],A[k])
				count=count+1
				#print(small)
				listOfList.append(small)
	#print(listOfList)
	# print("No of combi: %d"%(len(listOfList)))
	return listOfList



a=[1,2,3,4,5]
#Generate 3-digits number with and without repition
for x in genWithoutRep(a):
	print(x)
print("No of combi: %d"%(len(genWithoutRep(a))))

for x in genWithRep(a):
	print(x)
print("No of combi: %d"%(len(genWithRep(a))))


"""
Algo:
Generate 3-digits number with and 
without repition from given array{1,2,3,4,5}
Don't Memorize
4x3x2===>For non-repeting
4x4x4===>For repeting
Complexity:based on number digit to form a number

"""
