for i in range(100, 1000, 2):
    i = i + 1
print(i)
print("All the statements are getting printed")
print("This will not get printed inside the loop")

while i > 900:
    print("I is lesser than 900")
    i = i - 1
print("We are out of the while loop")
