#Built in Methods of dictionary

#copy
d={"name":"abhi","age":25}
print(id(d)) #2223825608704
d1=d.copy()
print(id(d1)) #2223826003328
#it is used for performing shallow copy.

#clear
d={"name":"abhi","age":25}
d.clear()
print(d) #{}

#keys
d={"name":"abhi","age":25}
print(d.keys()) #dict_keys(['name', 'age'])

#values
d={"name":"abhi","age":25}
print(d.values()) #dict_values(['abhi', 25])

#get
d={"name":"abhi","age":25}
print(d.get("name")) #abhi

#setdefault
d={"name":"abhi","age":25}
print(d.setdefault("age")) #25
print(d.setdefault("mob")) #None

#update
d={"name":"Abhi","age":25,"Name":"Babul","mob":None}
d.update({"mob":9876543210,"gender":"male"})
print(d) #{'name': 'Abhi', 'age': 25, 'Name': 'Babul', 'mob': 9876543210, 'gender': 'male'}

#pop
d={'Name': 'Abhi', 'age': 25, 'mob': 9876543210, 'gender': 'male'}
d.pop("Name")
print(d) #{'age': 25, 'mob': 9876543210, 'gender': 'male'}
d.pop("Email")
print(d) #Error

#popitems
d={'Name': 'Abhi', 'age': 25, 'mob': 9876543210, 'gender': 'male'}
print(d.popitem()) #('gender', 'male')
print(d) #{'Name': 'Abhi', 'age': 25, 'mob': 9876543210}

#formkeys
print({}.fromkeys('hai',0)) #{'h': 0, 'a': 0, 'i': 0}
print({}.fromkeys(['hai','bye','hello'])) #{'hai': None, 'bye': None, 'hello': None}
