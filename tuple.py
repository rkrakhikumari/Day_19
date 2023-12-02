#Tuple: immutable, ordered, allows duplicate elements
#my_tuple = tuple(["rakhi",5,"delhi"])
#print(my_tuple)
#item = my_tuple[0]
#print(item)

#for i in my_tuple:
 #   print(i)

#if "rakhi" in my_tuple:
 #   print("yes")
#else:
   # print("no")
#my_tuple = ('a','b','c','d','d')
#print(len(my_tuple))
#print(my_tuple.count('f'))
#print(my_tuple.index('a'))
#my_list = list(my_tuple)
#print(my_list)
#my_tuple2 = tuple(my_list)
#print(my_tuple2)

#a =(1,2,3,4,5,6,7,8,9,10)
#b = a[::-1]
#print(b)

#my_tuple = "rakhi",20,"delhi"
#name,age,place = my_tuple
#print(name)
#print(age)
#print(place)

#my_tuple = (0,1,2,3,4,5,6,7,8,9)
#x , *y,z = my_tuple
#print(x)
#print(y)
#print(z)

#import sys
#my_list = [0,1,2,3,"hello",True]
#my_tuple =(0,1,2,3,"hello",True)
#print(sys.getsizeof(my_list),"bytes")
#print(sys.getsizeof(my_tuple),"bytes")

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5,]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5,)", number=1000000))
