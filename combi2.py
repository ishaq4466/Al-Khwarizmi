class Solution:
	def combine(self,n,k):
		lista=[]
		self.backtrace(lista,[],n,k,0)
		return lista
	def backtrace(self,lista,tempList,n,k,pos):
		if len(tempList)==k:
			# print("Apended...")
			# print(tempList)
			lista.append(tempList[:])
		else:
			# print("Value of k:"+str(k))
			for i in range(pos,n):
				tempList.append(i+1)
				self.backtrace(lista,tempList,n,k,i+1)
				tempList.pop()


obj=Solution()
for x in obj.combine(22,11):
	print(x)


"""
def getCombi(arr,data,start,end,index,r):
	if index==r:
	# 	print("index=r")
		print(data)
		print()
		return 
	i=start
	print(">>>>>>>i=%d"%(i))

	while(i<=end and end-i+1>=r-index):
		# print("dta[index]=arr[i]")
		data[index]=arr[i]
		print("Data: "+str(data))
		print("index: "+str(index))

		getCombi(arr,data,i+1,end,index+1,r)
		i=i+1
		print("\ni=%d"%(i))


arr=[1,2,3,4,5,4,8,7,8,7,5,8,5,7,78,5,6,8,74,74,85]
n=len(arr) 	#5
r=11	#2
#5C2
data=[0]*r
#[0,0]
print(arr)
print(data)
print(n)
print(r)
print("==========================")
getCombi(arr,data,0,n-1,0,r)

# arr-->data
# dat-->temp array
# start 
# end
# Current index in data
# size of combinitions to be printed







Write Function to get nCr
e.g:
if a={1,2,3,4,5}
form 3digit num
O/p:1 2 3
{1 2 4},
{1 2 5},
{1 3 4}
{1 3 5},
{1 4 5},
{2 3 4},
{2 3 5},
{2 4 5},
{3 4 5}
Answer:5C3=10 possible combinitions


"""








