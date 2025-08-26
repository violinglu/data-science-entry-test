
def string_reverse(s):
    newlist=[]
    if isinstance(s,str):
        for x in s: newlist.append(x)
        newlist.reverse()
        for y in newlist: gsm="".join(newlist)
    else: print('input error')
    return gsm
 
print(string_reverse("Hello World"))
print(string_reverse("Python"))


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"def
