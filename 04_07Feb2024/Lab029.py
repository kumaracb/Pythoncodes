# String Concat
str1 = "Hello"
str2 = "Bangalore"
str3 = str1 + str2
print(str3)

name = "Kumara"
age = 38
# r = name + age  # TypeError: can only concatenate str (not "int) to str
r = name + str(age)
print(r)

g = "Hello"
g += "Bangalore"
# g = g + "Bangalore"
print(g)

# Increment and Decrement ++, --
x = 5
x-=1
print(x)

x = 10
# y = x+1
