def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    result_array1 = []
    for i in array1:
        result_array1.append(i ** 2)
    result_array1.sort()
    array2.sort()
    if result_array1 == array2:
        return True
    else:
        return False

print(comp([121, 144, 19, 161, 19, 144, 19, 11] , [121, 14641, 20736, 361, 25921, 361, 20736, 361]))
print(comp([] , None))