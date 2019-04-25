def getBxP(B,P):
#	print(B,P)
	return ((B[0]*P[1])-(B[1]*P[0]))
def shiftAtoOrigin(A,B,P):
	listOfTup=[]
	a1,a2=A[0],A[1]
	for x in [A,B,P]:
		 print(x)
		 x=(x[0]-a1,x[1]-a2)
		 print(x)
		 listOfTup.append(x)
	return listOfTup

def getSideOfP(A,B,P):
	shiftedPoints=shiftAtoOrigin(A,B,P)
	value=getBxP(shiftedPoints[1],shiftedPoints[2])	
	print(value)
	if value<0:
		print("P is on Left side")
	else:
		print("P is on right side")

A=(0,2)
B=(0,-1)
# P=(2,3)
P=(-2,0)
getSideOfP(A,B,P)

#	Algo:
#	1.Shift A to origin
#	2.Take BxP and check for negative value of BxP
# 	if BxP<0 i.e negative
# 	then P lies left side
# 	else: 
# 	then P lies right side
#
#			   ↑
# 			   |  B(1,4)
# 			   |  /\	
#        	   | /	\
#    	 O(0,0)|/____\A(3,1)
# ←------------.------------→
#  	    	   |
# 	    	   |
# 		       |
# 	       	   |
#			   ↓
# Test Cases:
# A=(-3,2)
# B=(3,2)
# # P=(2,3)
# P=(-2,-1)
# A=(-30,10)
# B=(29,-15)
# # P=(2,3)
# P=(15,28)
#BxP=BxPy-ByPx