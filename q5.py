def check_divisibility(num, divisor):
    try: 
       sat=num%divisor
       if sat==0: print ("True")
       else: print ("False")
    except ValueError: print("input error")
    return sat

print(check_divisibility(10,2))
print(check_divisibility(7,3))


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
