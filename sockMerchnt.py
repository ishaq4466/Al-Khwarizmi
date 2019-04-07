def sockMercharrnt(arr):
	socksDict={}
	for x in arr:
		if x not in socksDict:
			socksDict[x]=1
		else:
			socksDict[x]+=1
	return socksDict


sockPile=["red","blue","black","red","brown","black","gray"]#,1,2,8,4]
print("Sock Pile: "+str(sockPile))
socksDict=sockMercharrnt(sockPile)
#print(socksDict)
print("sock pile contains")
for k,v in socksDict.items():
	print("%d pair of %s socks"%(int(v)//2,k))




"""
I/P: [4,8,1,2,8,4]
No. reprents colors of socks
O/P: 2 pairs of socks are present in sock piles
"""

