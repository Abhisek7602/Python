# 1)Count
l=[12,"hai","bye",67,34]
print(l.count("bye"))
#1

# 2)Index
l=[12,"python","Abhi",56,90]
print(l.index(90))
#4

# 3)append
l=[12,"bye","Abhi",89,23]
l.append('hai')
l.append(34)
print(l)
#[12, 'bye', 'Abhi', 89, 23, 'hai', 34]

# 4)extend
l=[13,45,67,"hai","bye"]
l.extend("python")
print(l)
#[13, 45, 67, 'hai', 'bye', 'p', 'y', 't', 'h', 'o', 'n']

# 5)insert
l=[12,45,"hai","bye"]
l.insert(3,"Abhi")
print(l)
#[12, 45, 'hai', 'Abhi', 'bye']

#6)pop
l=[13,34,56,"bye","hai",99]
l.pop(3)
print(l)
#[13, 34, 56, 'hai', 99]
#If the index position is not avaliable it will throw an error.

#7)remove
l=[12,34,"hai","abhi"]
l.remove("hai")
print(l)
#[12, 34, 'abhi']
#If the value is not avaliable it will throw an error.

#8)clear
l=[12,34,"hai","bye"]
l.clear()
print(l)
#[]

#9)sort
l=[12,34,56,99,1]
l.sort()
print(l)#Ascending
#[1, 12, 34, 56, 99]

l1=[12,34,56,99,1]
l.sort(reverse=True)
print(l)#Desecending
#[99, 56, 34, 12, 1]

# 10)copy
l=[11,22,[45,67,90],78]
print(id(l))  #3159869269440
print(id(l[2]))  #3159869120576
NCL=l
print(id(NCL))  #3159869269440
print(id(NCL[2])) #3159869120576

# # 11)shallow copy
l=[11,22,[45,67,90],78]
print(id(l)) #1866572932544
print(id(l[2])) #1866572783680
SCL=l.copy()
print(id(SCL)) #1866572783680
print(id(SCL[2])) #1866572783680

# 12)Deep copy
l=[11,22,[45,67,90],78]
print(id(l)) #2440271209920
print(id(l[2])) #2440271061056
import copy
DCL=copy.deepcopy(l)
print(id(DCL)) #2440272860608
print(id(DCL[2])) #2440271063936


