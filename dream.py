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
a=[1.6, 5.4, 6.8, 9.0, 9.5, 4.3, 7.5, 6.9, 8.6, 10.1, 15.2, 12.6,1.5,1.2,1.6,1.9,1,5.6,1.8,2.6,3.6,8.9]
print("points:%s"%(a))
print("Lenght of points: "+str(len(a)))
print("============================================")

list1=genSet(a)


#print(list1)
print("============================================")
players=11
point=100
print("No of players: %d \nRequired point<=%d"%(players,point))
#print("No of players: %d \nRequired point=%d"%(players,point))
for elements in list1:
	if len(elements)==players and sum(elements)<=point:
		print("%s Tot_Points:[%d]"%(str(elements),sum(elements)))



