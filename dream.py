import random
def genSet(A):
 		if len(A)==0:
 			return [[]]
 		listOfElementsWithoutLastElement=genSet(A[:-1])
 		lastElement=A[-1:]
 		newList=[]
 		for x in listOfElementsWithoutLastElement:
 			newList.append(lastElement+x)
 		return newList+listOfElementsWithoutLastElement


#a=random.sample(range(1,10),22)
#random.shuffle(a)
#a=[float(x) for x in input().split()]
#print(a,a[:-1],a[-1:])
#a=['a','b','c','d','e','f','g','f','h']
a=[9.5,9.5,9,11,9.5,8.5,8.5,9.0,8.5,8.5,8.5]
b=sorted(a,reverse=True)
print("points:%s"%(a))
print("points:%s"%(b))
c=a+b
print("points:%s"%(c))

print("Total length of points: "+str(len(a+b)))
print("============================================")
list1=genSet(c)

#print(list1)
print("============================================")
players=11
point=100
#print("No of players Required: %d \nRequired point<=%d"%(players,point))
print("No of players: %d \nRequired point=%d"%(players,point))
for elements in list1:
	if len(elements)==players and sum(elements)==point:
		print("%s Tot_Points:[%d]"%(str(elements),sum(elements)))



