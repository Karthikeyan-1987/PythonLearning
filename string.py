str1="Ilakkiya"
str2=str("Ilakkiya")

print(id(str1),"\n",id(str2))

str2+=str2+" Chandran"

#str2 value changed, hence address also changed
print(id(str1)," ",id(str2))
