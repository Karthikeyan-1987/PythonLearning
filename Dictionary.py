# Initializing Dictionary
City = {'svks': '626123', 'chn': '600059', 'irving': '75063', 'saint': '63021'}
print(City)

# Adding New Key Value
City['madurai'] = '73222'
print(City)

# Modifying Existing Value
City['madurai'] = '625001'
print(City)

# Deleting Key Value
del City['saint']
print(City)

# Retriving Key Value
print(City['svks'])

# Looping Items in the Dictionary
for x in City:
    print(x, ":", City[x])

# Length of the Dictionary
print("Length of the Dictionary\t", len(City))

# Equality Operator
print(City == City)
BigCity = City
print(BigCity != City)
BigCity["Chicago"] = "213455"
print(BigCity,"\n",City)
print(BigCity == City)

#Dictionary Methods
print(City.popitem(), "\n",City) #removing the Last item in the dictionary. LIFO
print(City.keys()) #Printing just the keys
print(BigCity.values()) #Printing just the values
print(City.get("svks")) #Display the value for the key
print(City.pop("svks"),"\n",City) #Removing the element from the dictionary
BigCity.clear() #Empty the dictionary
print(BigCity)
