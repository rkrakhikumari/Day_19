#from itertools import product
#a = [1,2]
#b = [3,4]
#prod = product(a,b)
#print(list(prod))

#from itertools import combinations, combinations_with_replacement
#a = [1,2,3,4]
#comb = combinations(a,2)
#print(list(comb))
#comb_wr = combinations_with_replacement(a,2)
#print(list(comb_wr))

#from itertools import accumulate
#a = [1,2,3,4]
#acc = accumulate(a)
#print(a)
#print(list(acc))

#from itertools import accumulate
#import operator
#a = [1,2,3,4]
#acc = accumulate(a, func=operator.mul)
#print(a)
#print(list(acc))

#from itertools import groupby

#def smaller_than_3(x):
   # return x < 3
#a = [1,2,3,4,5]
#group_obj = groupby(a, key=lambda x:x<3)
#for key, value in group_obj:
   # print(key, list(value))

#from itertools import groupby
#persons = [{'name':'tim','age':20},{'name':'dan','age':20},
        #  {'name':'lisa','age':21},{'name':'kaili','age':22}]
#group_obj = groupby(persons, key=lambda x: x['age'])
#for key, value in group_obj:
    #print(key,list(value))
#from itertools import count,cycle,repeat
#for i in count(10):
    #print(i)
    #if i == 15:
        #break

#a = [1,2,3]
#for i in cycle(a):
    #print(i)

#a = [1,2,3]
#for i in repeat(1):
    #print(i)
