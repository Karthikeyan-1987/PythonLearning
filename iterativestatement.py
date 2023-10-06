for i in range(100, 1000, 2):
    print("Before increment",i)
    i = i + 3
    print("After increment",i)
print("All the statements are getting printed")
print("This will not get printed inside the loop")

while i > 900:
    print("I(%d) is greater than 900"%i)
    i = i - 1
print("We are out of the while loop and I(%d) is NOT greater than 900"%i)
