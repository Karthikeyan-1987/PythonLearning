#Begining with Sample List
List1=list()
print(List1)

List2= list([1,2,3,4,5])
print(List2)
print(List2.reverse())

List3=["Karthi","Karthi","Ilakkiya","Dhiya","Shri"]
print(List3)

List4=list("Karthikeyan")
print(List4)

List5=list([1,2,"Kumar",3,"Ramesh"])
print(List5)

List6=list("12345")
print(List6)

#Common List Operations
print("#Common List Operations:")
print("3" in List6)
print("Raj" not in List5)
print(len(List2))
print(max(List3))
print(min(List6))
print(min(List3))
print(sum(List2))

#List Slicing
print("#List Slicing:\n")
print(List1[:3])
print(List2[2:])
print(List3[1:5])
print(List4[::-1])
print(List4[:])

#+ AND * Operators in List
print("\n#+ AND * Operators in List")
List42=List4+List2
print(List42)

List32=List3*3
print(List32)

#for loop with List
print("\n#for loop with List")
for i in List6:
    print(i,end=" ")

List7=([2,3,5,11,99,3,1])
#Commonly Used List Functions
print("\n#Commonly Used List Functions")
print(List6.append(6))  #Returns None
print(List3.count("Karthi")) #returns index positions
print(List2.pop(2)) #returns the element at specified index
print(List3.index("Shri")) #returns the index for the given element
print(List7.sort(), List7) #sort the list
print(List6.reverse()) #reversing the elements in the list
print(List1.insert(2,"Python",),List1) #retuns none
print(List6.remove(6), List6) #retuns None
print(List42.extend(List32), List42) #adding the List32 to List42. It retunr

#List Comprehension with for Loop
print("\n#List Comprehension with for Loop")
NewList1=[x for x in range(20)]
print(NewList1)
NewList2=[x+1 for x in range(20)]
print(NewList2)
NewList3=[x for x in range(20) if x%2==0]
print(NewList3)
