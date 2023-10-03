a = 10

for i in range(20):
    if i == 3:
        print("Number %d is NOT Printed" %i)
        continue
    if i == 13:
        print("Loop is broken")
        break
    print(i)

