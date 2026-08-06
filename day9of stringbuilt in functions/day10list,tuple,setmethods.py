'''
a=[10,20,30]
print(a)
#operations on list
a=[10,20,30]
b=[40,50,60]
print(a+b)#concatination
print(a*3)#repetition
print(a[0])#indexing
print(a[0:2:1])#slicing
print(a[::1])
'''
'''
#functions of list
a=[10,20,30]
print(min(a))
print(max(a))
print(len(a))
print(sum(a))
print(any(a))
print(all(a))
'''
'''
#methods of list
a=[10,20,30]
print(a)
print(a.append(40))
print(a)
print(a.extend([35,45]))
print(a)
print(a.index(a[0]))
print(a.pop(1))
print(a.sort())
print(a)
print(a.reverse())
print(a)
print(a.clear())
print(a)
'''

#operations on tuple
'''
a=(10,200,300)
print(a)
b=(2000,3000,4000)
print(b)
print(a+b)#concatination
print(a*50)#repitition
print(a[0:1:1])#slicing
print(b[0:4:2])
print(any(a))
print(all(a))
'''
'''
#tuple methods
#count()
#index()
a=(10,20,30,10)
print(a.count(10))
print(a[0])
print(a[1])
print(sum(a))
print(sorted(a))
'''
'''
#operations on set
a={10,20,4000000000}
print(a)
b={200000000,300000000,50000000}
print(a|b)
print(a&b)
print(a>=b)
print(a<=b)
print(a.isdisjoint(b))
print(a^b)
print(a-b)
'''
#methods of sets
a={10,2,3}
b={2,3,4}
print(a)
print(a.add(102))
print(a)
print(a.update([5,6]))
print(a.remove(102))
print(a.pop())
print(a<=b)