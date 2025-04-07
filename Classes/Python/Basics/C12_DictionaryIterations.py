fruits = {"apple":"red", "grapes":"black", "lemon":"green", "banana":"yellow"}

#Iterate fruits over keys
print("Example to Iterate 'keys' of fruits")
for key in fruits:
    print(key)

print("Example to Iterate 'values' of fruits")
for value in fruits.values():
    print(value)

print("Example to Iterate 'keys and values' of fruits")
for key,value in fruits.items():
    print(key,value)