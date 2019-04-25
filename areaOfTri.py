def getCross(A,B):
#	print(round((A[0]*B[1])+(A[1]*B[0]),2))
	return round(((A[0]*B[1])-(A[1]*B[0])),2)

def getAreaOfTri(vertices):
	crossPro=abs(getCross(vertices[0],vertices[1]))
	return round((crossPro/2),2)

A=(3,1)
B=(1,4)
points=[A,B]

print("Vertex A: %s\nVertex B: %s\nArea:%0.2f Units"%(str(A),str(B),getAreaOfTri(points)))


# Print the area for triagle for Points
# O(0,0) A(3,1) B(4,1)
# i.e one of the point @ origin

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
# Algo:
# Simply take cross-Product of AxB and divide it by 2
# since O is at origin
# AxB=AxBy-AyBx
