
# The goal is to order as many pizza slices as possible, but not more than the maximum number
# i/p:
# 17 4 M=17 N=4  
# 2 5 6 8
# o/p
# 3
# 2 6 8


def get_max_slices(pizza_type_list,max_slices):
		print(sum(pizza_type_list))



# max_slices,pizza_type=input().split()
max_slices=17
pizza_type=4
print("Max Slices: {0}".format(max_slices))
print("Pizzas Type:{0}".format(pizza_type))

# pizza_type_list= input().split()
pizza_type_list = [2,5,6,8]
print("No of slices in each pizzaz: "+str(pizza_type_list))



print(get_max_slices(pizza_type_list, max_slices))













