# Task 1
#   - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
#    - lst must be a list.
#    - Return the modified list.
# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

def find_and_replace(lst, find_val, replace_val):
    if type(lst)!=list: print ("error: this is not a list")
    else:
        for x in lst:
            if x == find_val: 
               a=lst.index(x)
               lst[a]=replace_val
            
            else: continue
        
    return(lst)

print(find_and_replace([1,2,3,4,2,2],2,5))
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))
