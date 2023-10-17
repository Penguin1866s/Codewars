def first_n_smallest(arr, n):
    arr_original = arr[:]
    while len(arr) != n:
        arr.remove(max(arr))
    
    if len(arr) == len(set(arr)):
        arr_result1 = arr
        return arr_result1
    else:
        arr_result2 = []
        k = -1
        for i in arr_original:
            if len(arr_result2) != n:
                if i == arr[k]:
                    k += 1
                    arr_result2.append(i)
                else:
                    continue
            else:
                break
        return arr_result2



#rint(first_n_smallest([1,2,3,1,2] , 3))
#print(first_n_smallest([1,2,3,4,1] , 3))
print('\n\n')
print(first_n_smallest([5, 4, 3, 2, 1],3))
#first_n_smallest([1,2,3,4,5],3) == [1,2,3]
"""
    arr.sort()
    arr.reverse()
    while len(arr) > n:
        arr.remove(arr[0])
    arr.reverse()
    return arr"""