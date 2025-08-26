def update_dictionary(dct, key, value):
    
    for k in dct:
        if k == key: 
            print(key,dct[key])
            dct[key]=value
    dct.update({key:value})
    return dct

print(update_dictionary({},"name","Alice"))
print(update_dictionary({"age":25},"age","26"))

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26
