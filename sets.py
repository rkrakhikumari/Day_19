#Sets :unordered,mutable,no duplicates
#myset = {1,2,3,2,3}
#print(myset)
#myset =set("hello")
#print(myset)
#myset = set()
#myset.add(1)
#myset.add(2)
#myset.add(3)
#myset.discard(4)
#print(myset)
#for x in myset:
    #print(x)
#if 1 in myset:
   # print("yes")
#odds ={1,3,5,7,9}
#evens ={2,4,6,8,10}
#primes ={2,3,5,7}
#u = odds.union(evens)
#print(u)
##i = odds.intersection(evens)
#i = odds.intersection(primes)
#print(i)
#setA ={1,2,3,4,5,6,7,8,9}
#setB ={4,5,6,7}
#diff = setA.difference(setB)
#diff = setB.symmetric_difference(setA)
#print(diff)
#setA.update(setB)
#print(setB.issubset(setA))
#print(setA.issuperset(setB))
#setB = set(setA)
#setB.add(10)
#print(setA)
#print(setB)
a = frozenset({1,2,3,4,5})
print(a)