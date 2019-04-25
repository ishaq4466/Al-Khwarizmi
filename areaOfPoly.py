def getCross(A,B):
	# print(round((A[0]*B[1])+(A[1]*B[0]),2))
	return round(((A[0]*B[1])+(A[1]*B[0])),2)

def getAreaOfTri(vertices):
	crossPro=abs(getCross(vertices[0],vertices[1]))
	return round((crossPro/2),2)

def getAreaOfPoly(points,n):
	sumOfAllArea=0
	for i in range(n-1):
		print(points[i],points[i+1],getAreaOfTri([points[i],points[i+1]]))
		print()
		sumOfAllArea+=getAreaOfTri([points[i],points[i+1]])

	print(points[n-1],points[0],getAreaOfTri([points[n-1],points[0]]))
	sumOfAllArea+=getAreaOfTri([points[n-1],points[0]])

	print(sumOfAllArea)
	return sumOfAllArea

A=(-3,-2)
B=(3,1)
C=(2,3)
D=(-2,1)
points=[A,B,C,D]
edges=len(points)
print("Addition of all area of tri i.e area of polygon: "+str(getAreaOfPoly(points,edges)))




# Write a function to calculate area of polygon with 'n' edges
# Algo:
# Simply Break the polygon into triagle's and at the 
# end add all those areas 

