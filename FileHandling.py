#Writing data into a file
fil = open("C:\KARTHIKEYAN\Python\sample.py.txt", "w")
fil.write("This is through python programming -first\n")
fil.write("This is through python programming - Second\n")

#Reading date from a file
fil = open("C:\KARTHIKEYAN\Python\sample.py.txt", "r")
print(fil.read(10)) #retuns the specified number of characters from the file from index 0.
print(fil.read())  #read retuns all the content of the file if the index is not specified. Here same object fil is used. so it returns the content from where it left on the previously used statement

fil2 = open("C:\KARTHIKEYAN\Python\sample.py.txt", "r")
print(fil2.readline()) #readline() returns one line at a time
fil2.newlines
print(fil2.readline())

fil1 = open("C:\KARTHIKEYAN\Python\sample.py.txt", "r")
print(fil1.readlines()) #readlines() retuns all the lines in List Type
fil.close()
fil1.close()

#Appending data to EOF
file_append=open("C:\KARTHIKEYAN\Python\sample.py.txt", "a")
file_append.write("This is for End of File Statement")
file_append.close()

#Reading data line by line through for loop
file_read_loop = open("C:\KARTHIKEYAN\Python\sample.py.txt", "r")
for file in file_read_loop:
    print(file)
