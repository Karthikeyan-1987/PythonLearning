a = 10

for i in range(20):
    if i == 3:
        print("Number %d" % i, " is NOT Printed")
        continue
    if i == 13:
        print("Loop is broken")
        break
    print(i)
