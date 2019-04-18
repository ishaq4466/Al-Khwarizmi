import random
def getList(A):
	returnList=[]
	for i in range(len(A)):
		#print(A[i])
		for  x in A[i]:
			returnList.append(x)
	#print(returnList)	
	return returnList

def getPlayersNme(A,D):
	retDict={}
	#for k,v in D.items():
	for k,v in zip(D.keys(),A):
		if v not in retDict:
			retDict[v]=[k+"("+str(v)+")"]

		else:
			#retDict[v].append(k)
			retDict[v].append(k+"("+str(v)+")")
#	print(retDict)
	return getList(retDict.values())

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
# print(a.split())
#print(a,a[:-1],a[-1:])
#a=['a','b','c','d','e','f','g','f','h']
a=[9.5,9.5,9,11,9.5,8.5,8.5,9.0,8.5,8.5,8.5]

b=sorted(a,reverse=True)
print("points:%s"%(a))
print("points:%s"%(b))
points=a+b
names=["AmbatiRayudu",
"FafDuPlessis",
"KedarJadhav",
"MuraliVijay",
"SureshRaina",
"DavidWilley",
"DwayneBravo",
"MitchellSantner",
"RavindraJadeja",
"ShaneWatson",
"MSDhoni"
]
names+=[
"ChrisLynn",
"JoeDenly",
"NitishRana",
"RinkuSingh",
"RobinUthappa",
"ShubmanGill",
"AndrRussell",
"CarlosBrathwaie",
"DineshKarthik",
"NikhilNaik",
"HarryGurney"
]

print("points:%s"%(points))
print(names)
print("Total length of points: "+str(len(points)))
print("============================================")
players={}
for k,v in zip(names,points):
	players[k]=v

for k,v in players.items():
	print("%s 				%0.1f"%(k,v))
	
print("============================================")

list1=list(players.values())
print(list1)	
print("============================================")

list2=genSet(list1)

#print(list32)
print("============================================")
players=11
point=100
#print("No of players Required: %d \nRequired point<=%d"%(players,point))
print("No of players: %d \nRequired point=%d"%(players,point))
for elements in list2:
	if len(elements)==players and sum(elements)==point:
		#print("%s Tot_Points:[%d]"%(str(elements),sum(elements)))
		print(getPlayersNme(elements,players))


