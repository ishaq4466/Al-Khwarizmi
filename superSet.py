import random

def genSubset(A):
	if len(A)==0:
		print("Last Recursive Call..returns [[]]")
		return [[]]

	listWithoutLstElemnt=genSubset(A[:-1])
	print("listWithoutLstElemntToAdd: "+str(listWithoutLstElemnt))
	lastElemntToAdd=A[-1:]
	print("ElemntToAdd %s in returned list %s"%(str(lastElemntToAdd),str(listWithoutLstElemnt)))
	new=[]
	for x in listWithoutLstElemnt:
		new.append(x+lastElemntToAdd)
	print("new list after adding:"+str(new))
	print("Finally returning newlist + listWithoutLstElemntToAdd: "+str(new+listWithoutLstElemnt))
	print("============================================")
	return new+listWithoutLstElemnt



a=random.sample(range(1,5),4)
#print(genSubset(a))
print(a)
# print(a[:-1])
# print(a[-1:])
print("=============================================")
print("Finally we got our power set: "+str(genSubset(a)))
