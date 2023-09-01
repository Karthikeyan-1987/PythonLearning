a = input("Enter A\n")

if int(a) % 2 == 0:
    print("Even\n")
    a = 20
    print("Printing a", a)
elif int(a) % 2 != 0:
    print("Odd\n")
else:
    print("This is not part of If statements")

print("Even Number") if int(a) % 2 == 0 else print("Odd Number")

{print("Even"), print(" Number")} if int(a) % 2 == 0 else {print("Odd"), print(" Number")}
