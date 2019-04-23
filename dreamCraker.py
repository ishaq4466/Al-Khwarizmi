#listOfPoints PlayrsDict
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

def whtherToShow(elementList):
#Seven Possible combinitions
	# reqComb=[
	# [1.0,3.0,2.0,5.0],
	# [1.0,3.0,3.0,4.0],
	# [1.0,4.0,1.0,5.0],
	# [1.0,4.0,2.0,4.0],
	# [1.0,4.0,3.0,3.0],
	# [1.0,5.0,1.0,4.0],
	# [1.0,5.0,2.0,3.0]
	# ]
	#,[2,7,1,1]]
	plyTypeDict={"WK":0.0,"BOWL":0.0,"BAT":0.0,"AR":0.0}
	for a in elementList:
		#matches=[]
		for x in plyTypeDict.keys():
			if x in a:# and x not in matches:
				#matches.append(x)
				plyTypeDict[x]+=1;
	return plyTypeDict,plyTypeDict.values
	#print("%s 	%s"%(plyTypeDict,plyTypeDict.values()))
	# print(plyTypeDict)
	# print(plyTypeDict.values())
	# return plyTypeDict.values() in reqComb



def getnCr(A):
 		if len(A)==0:
 			return [[]]
 		X1=getnCr(A[:-1])
 		lastElement=A[-1:]
 		newList=[]
 		for x in X1:
 			newList.append(lastElement+x)
 		return newList+X1



a=[8.5,8.5,8.0,8.0,9.0,8.5,10.5,9.0,9.0,9.5,9.0]#KKRCredits
b=[8.5,8.0,8.5,8.0,8.5,8.5,9.0,8.0,10.0,11.0,8.5]#RCBCredits
#b=sorted(a,reverse=True)
print("Credit_List1:%s"%(a))
print("Credit_List2:%s"%(b))
points=a+b

#KKR
names=[
"PChawla[BOWL]",
"HGurni[BOWL]",
"SGill[BAT]",
"PKrishna[BOWL]",
"NRana[BAT]",
"kuldeep[BOWL]",
"ARussel[AR]",
"SNarayan[AR]",
"RUttappa[BAT]",
"CLynn[BAT]",
"DKartik[WK]"
]

#RCB
names+=[
"UmeshY[BOWL]",
"NSaini[BOWL]",
"DStane[BOWL]",
"PNegi[BOWL]",
"YChawla[BOWL]",
"MoinALI[AR]",
"MKRStownis[AR]",
"AkashDeepN[BAT]",
"ABDVillers[BAT]",
"VKholi[BAT]",
"PPatel[WK]"
]


players={}
for k,v in zip(names,points):
	players[k]=v

print("================================================================")
for k,v in zip(names,points):
		print("%s 				%0.1f"%(k,v))



print("============================================")

list1=list(players.values())
print("TotalCredits: "+str(list1))	
print("============================================")

list2=getnCr(list1)
#points=[9.5,9.5,9,11,9.5,8.5,8.5,9.0,8.5,8.5,8.5]
#print(list32)
print("============================================")
players1=11
point=100
#print("No of players Required: %d \nRequired point<=%d"%(players,point))
print("No of players: %d outOf 22 \nRequired point=%d"%(players1,point))
# for elements in list2:
# 	if len(elements)==players1 and sum(elements)<=point:
# 		#print("%s Tot_Points:[%d]"%(str(elements),sum(elements)))
# 		#print("%s Tot_Points:[%d]"%(getPlayersNme(elements,players),sum(elements)))
# 		print("%s Tot_points:[%d]"%(getPlayersNme(elements,players),sum(elements)))


#Getting the no of WC,BAT,BOWL,AR
for elements in list2:
	if len(elements)==players1 and sum(elements)<=point:
		#print("%s Tot_Points:[%d]"%(str(elements),sum(elements)))
		#print("%s Tot_Points:[%d]"%(getPlayersNme(elements,players),sum(elements)))
		print("%s 	%s 		Tot_points:[%d]"%(getPlayersNme(elements,players),whtherToShow(getPlayersNme(elements,players)),sum(elements)))









