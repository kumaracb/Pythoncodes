name = "Kumar"
name2 = 'Kumara'

print(len(name))  # len -> 1
print((name)[4])

#print(name[6]) # IndexError: string index out of range

print(len(name)-1)
print(name[len(name)-1])

# String - Immutability
# that can't be changed, modify
string = "Hello"
string = "Kumara"
print(string)
#string[0] = "P" #Typeerror: 'str object does not support item assignment
