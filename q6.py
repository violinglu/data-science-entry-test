def find_first_negative(lst):
    lst_size=len(lst)
    i=0
    while i<lst_size:
        a=lst[i]
        if a<0: return(a)
        i +=1
       
    return "no negatives"

print(find_first_negative([3,5,-1,7,-2,8]))
print(find_first_negative([2,10,7,0]))
# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]
