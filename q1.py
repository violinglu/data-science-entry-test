# task 1
def swap(x,y):
    try:
        diff = float(x)- float(y)
        print (y,x)
    except ValueError:
        print ("-1")
    return
# task 2
print (swap("Apple",10))
print (swap(9,17))
