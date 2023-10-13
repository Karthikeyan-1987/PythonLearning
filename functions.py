def myfunction(start, end):
    output = 0
    for i in range(start, end):
        output += i
    print(output)


def sum1(start, end):
    output = 0
    for i in range(start, end):
        output += i
    return output


myfunction(1, 4)
print(sum1(1, 11))


# Example of Positional Arguments
def withdefaultvalues(i, j=10):  #2nd Parameter is the default argument. So, 10 will be assigned to j if no arguments passed from function
    print(i, j)


def withdefaultvalues1(i, j, z):
    print(i, j, z)


withdefaultvalues(1)  # With Just 1 Parameter and for the other one will be assigned with the default value
withdefaultvalues(1, 100)

# Example of Keyword Arguments
withdefaultvalues(i=2, j=30)  # Can pass the argument in any order in Keyword Arguments
withdefaultvalues(j=2, i=30)
withdefaultvalues1(10, z=30, j=100)  # Can be used with mix of positional and keyword arguments

# Returning multiple values
def multiplereturn(a):
    if a == 1:
        return 10, 20, 30
    else:
        return 1, 2, 3, 4, 5

tup=multiplereturn(2)
print(type(tup),tup)
