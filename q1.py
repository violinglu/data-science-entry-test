def swap(x,y):
    try:
        diff = float(x)- float(y)
        print (y,x)
    except ValueError:
        print ("-1")

print (swap("Apple",10))
print (swap(9,17))
