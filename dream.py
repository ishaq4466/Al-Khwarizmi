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


a=random.sample(range(1,10),6)
random.shuffle(a)
a=[2.5,1.5,1.5]
print(a,a[:-1],a[-1:])
#a=['a','b','c','d','e','f','g','f','h']
print("============================================")
list1=genSet(a)

print(list1)
print("============================================")

for elements in list1:
	if len(elements)==3 and sum(elements)<100:
		print(elements)
