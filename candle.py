def birthdayCakeCandles(ar):
	maxHightCandle=max(ar)
	noOfCndles=0
	for x in ar:	
		if(x==maxHightCandle):
			noOfCndles+=1
	return noOfCndles










a=[4,4,5,1,8,7,8,9,50,50]

print(birthdayCakeCandles(a)) #Required output

print("Candles with there heights: "+str(a))
print("Number of Candle that will be Blown is "+str(birthdayCakeCandles(a))+" of maximum htght "+str(max(a)))
#Required output



"""
Algo:

Step0:Initiaze mxHightdCndle,noOfCandleBlownd=0
Step1: 
Find the maximum highted candle(mxHightdCndle) from arr
Step2 :
Loop from i=0 to i=n-1:
	if arr[i]==mxHightdCndle:
		noOfCandleBlownd<-noOfCandleBlownd+1
Step 3: Return noOfCandleBlownd

O(n)
"""