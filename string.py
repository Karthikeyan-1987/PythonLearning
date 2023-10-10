str1="Ilakkiya"
str2=str("Ilakkiya")

print(id(str1),"\n",id(str2))

str2+=str2+" Chandran"

#str2 value changed, hence address also changed
print(id(str1)," ",id(str2))

#string multiplication
print((str1+" ") *10)

#String Slicing using Slicing[] Operators
print(str1[0:6]) #Ilakki
print(str1[1:3]) #la
print(str1[:7]) #Ilakkiy 
print(str1[0:-1]) #Ilakkiy
print(str1[0:-2]) #Ilakki

#ord() for ASCII code & chr() for ASCII
print("#ord() for ASCII code & chr() for ASCII:")
print(ord('a'))
print(chr(65))

#string functions
print("String Functions:")
print(len(str1))
print(max(str1))
print(min("Ilakkiya"))

#IN/NOT IN Operators
print("IN/NOT IN Operators:")
print('ki' in str1)
print('ki' not in str1)
print('zz' not in str1)

#Comparison Operators
print("#Comparison Operators:")
print("toy"=="toe")
print("Aa" > "aA")
print("Aa" < "aA")
print("A" <= "a")

#Iterating String with Loop
print("\n#String Manipulation with Loop:")
for i in str1:
    print(i)
    print(i,end="\n")
    print(i,end=" ")
    print(i,end="foo")

#Testing Strings
print("\n#Testing Strings")
print("str1".isalnum())
print(str1.isalpha())
print(str1.isdigit())
print(str1.isidentifier())
print(str1.isnumeric())
print(str1.islower())
print(str1.isupper())


#Searching for Substring
print("#Searching for Substring:\n")
print(str1.startswith("Ila"))
print(str1.endswith("y"))
print(str1.find("k"))
print(str1.rfind("k"))
print(str1.count("k"))

#Converting Strings
print("#Converting Strings:")
print("ilakkiya".capitalize())
print(str1.swapcase())
print(str1.replace("Ila","kar"))
