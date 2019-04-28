def getType(a,index):
	# print(index)
	return a[index:index+3]

def getLength(a,index):
	# print(index)
	return a[index:index+3]

def  getDta(a,index,tLenght):
	# print(index)
	# print(int(tLenght))
	return a[index:index+int(tLenght)]


def getRec(a):
	tType=""
	tLenght=0
	tDta=""
	# print(data)
	for x in a:
		index=0
		data=[""]*100 # Its an array of String with 100 elements 
		print(">>>>>>"+x+"<<<<<<<")
		while index<len(x):
			tType=getType(x,index)
			# print("TagType:"+tType)
			index+=3
			# print(index)
			tLenght=getLength(x,index)
			# print("TagLenhth:"+tLenght)
			index+=3
			# print(index)
			tDta=getDta(x,index,tLenght)
			# print("tagData:"+tDta)
			index+=int(tLenght)
			# print(index)
			data[int(tType)]=tDta  
		print("<<<<<<<<<<< "+'|'.join(data)+" >>>>>>>>")
		print()

a=["000002SH002003KIW001005HIJKL008015JKIOL458POI1234",
"001002KJ003003KIL"]
getRec(a)






