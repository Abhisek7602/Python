# 1)Lower
s="Abhisek"
print(s.lower())

# 2)Upper
s="Abhisek"
print(s.upper())

# 3)Title
s="aBHISEk"
print(s.title())

# 4)Capitalize
s="Abhisek"
print(s.swapcase())

# 5)islower
s="abhisek"
print(s.islower())

# 6)isupper
s="ABHISEK"
print(s.isupper())

# 7)istitle
s="Abhisek"
print(s.istitle())

# 8)isalpha
s="Abhisek"
print(s.isalpha())

# 9)isdigit
s="2345"
print(s.isdigit())

# 10)isalnum
s="Abhi345"
print(s.isalnum())

# 11)isspace
s="Abhi   "
print(s.isspace())

# 12)strip
s="Hello Abhisek   "
print(s.strip())

s1="-----Bye Abhisek-------"
print(s1.strip("-----"))

# --lstrip
s="======Abhisek"
print(s.lstrip("===="))


#--rstrip
s="Abhisek======"
print(s.rstrip("===="))

# 13)split
s="hai python"
print(s.split("y"))

# rsplit
s="hei Abhisek"
print(s.rsplit("e"))


# 14)repalce
s="hai python"
print(s.replace("h","k"))

# 15)count
s="hi Abhisek"
print(s.count("A"))
print(s.count("h",0,1,))

# 16)Index
s="hai abhisek how are you"
print(s.index("i"))
print(s.rindex("a"))

# 17)Find
s="Hai Abhisek"
print(s.find("b"))
print(s.rfind("se"))

# 18)startswith
s="hai python"
print(s.startswith("h"))

# 19)endswith
s="hai python"
print(s.endswith("n"))

# 20)format
s='this is {} and he is from {}'.format("Abhisek","Odisha")
print(s)

s1='this is {1} and he is from {0}'.format('Odisha',"Abhisek")
print(s1)

s2='this is {n} and he is from {p}'.format(p='odisha',n="Abhisek")
print(s2)

n="Abhisek"
p="Odisha"
s3=f'this is {n} and he is from {p}'
print(s3)

n=input("Enter your name:-")
p=input("Enter your Place:-")
s4=f'this is {n} and he is from {p}'
print(s4)

#Join
s="#".join("Abhisek")
print(s)