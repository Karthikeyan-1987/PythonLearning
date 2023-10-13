#Tuples are immutable, so addition, removal and deletion of tuples is not possible

# Different ways of creating tuples
tup1 = ()
print(tup1)
tup2 = (1, 2, 3, 4, 5)
print(tup2)
tup3 = tuple([1, 2, 3, 4, 5])
print(tup3)
tup4 = tuple("karthikeyan")
print(tup4)
tup5 = ("Ilakkiya")
print(tup5)

# Aggrate Functions with Tuples
print(len(tup1))
print(sum(tup2))
print(min(tup3))
print(max(tup4))
print(len(tup5))

#Iterating through Tuples
for x in tup2:
    print(x,end=" ")

print(tup2.count(1))  #Count elements in the tuples

#Slicing Tuples
print("#Slicing Tuples:")
print(tup2[0:4])
print(tup3[:3])

#in and not in operators
print(6 in tup2)
print(5 not in tup3)
