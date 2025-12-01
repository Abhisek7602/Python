#Built in methods of set

#copy
s={12,34,56,"hai","python"}
print(id(s)) #2234066010848
SCL=s.copy
print(SCL)
print(id(SCL)) #2234065919472
#It is used for performing shallow copy.

#Clear
s={12,34,67,"hai","Abhisekq"}
s.clear()
print(s) #set()

#add()
s={'python','bye',23,56,78,56}
s.add(50)
print(s) #{50, 23, 'bye', 56, 'python', 78}
#It will add the value randomly.

#Pop
s={"hai",33,"hello",100,190,20}
print(s.pop()) #hai
print(s) #{33, 'hello', 100, 20, 190}

#remove
s={"hello",34,'bye',45,56,78,23}
s.remove(34)
print(s) #{'bye', 23, 56, 'hello', 45, 78}
# s.remove(100) #keyError

#discard
s={"hyy","bye","hello",78,56,12}
s.discard("hyy")
print(s) #{56, 'hello', 12, 78, 'bye'}
s.discard("Abhi") #No Operations

#union
s={11,22,33}
s1={22,44,66}
s2={44,100,200}
print(s.union(s1)) #{33, 66, 22, 11, 44}
print(s2.union(s2)) #{200, 100, 44}

#intersection
s={11,22,33}
s1={22,44,66}
print(s.intersection(s1)) #{22}

#difference
s={11,22,33}
s1={22,44,66}
print(s.difference(s1)) #{33, 11}

#symmetric-difference
s={11,22,33}
s1={22,44,66}
print(s.symmetric_difference(s1)) #{33, 66, 11, 44}

#update
s={11,22,33}
s1={22,44,66}
s.update(s1)
print(s) #{33, 66, 22, 11, 44}

#intersection-update
s={11,22,33}
s1={22,44,66}
s.intersection_update(s1)
print(s) #{22}

#symmetric-difference-update
s={11,22,33}
s1={22,44,66}
s.symmetric_difference_update(s1)
print(s) #{33, 66, 11, 44}

#issuper
s={11,22,33}
s1={11,22}
print(s.issuperset(s1)) #True

#issubset
s={11,22,33}
s1={11,22}
print(s.issubset(s1)) #False

#isdisjoint
s={11,22,33}
s1={11,22}
print(s.isdisjoint(s1)) #False
