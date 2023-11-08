def fifo(n, reference_list):
    list_fifo = []
    k = 0
    for element in reference_list:
        if len(list_fifo) < n:
            if element not in list_fifo:
                list_fifo.append(element)
            else:
                continue
        elif k < n:
            if element not in list_fifo:
                list_fifo[k] = element
                k += 1
            else:
                continue
        else:
            k = 0
            if element not in list_fifo:
                list_fifo[k] = element
                k += 1
            else:
                continue
        continue
    if len(reference_list) < n or len(list_fifo) < n:
        while len(list_fifo) < n:
            list_fifo.append(-1)
    else:
        pass
    return list_fifo


#Test with assertions:
#test1:
assert fifo(3, [1, 2, 3, 4, 2, 5]) == [4, 5, 3] , "didn't pass the Test1: the result it has to be '[4, 5, 3]' not {}".format(fifo(3, [1, 2, 3, 4, 2, 5]))

#test2:
assert fifo(5, []) == [-1, -1, -1, -1, -1] , "didn't pass the Test2: the result it has to be '[-1, -1, -1, -1, -1]' not {}".format(fifo(5, []))

#test3:
assert fifo(4, [1, 2, 3, 3, 4, 5, 1]) == [5, 1, 3, 4] , "didn't pass the Test3: the result it has to be '[5, 1, 3, 4]' not {}".format(fifo(4, [1, 2, 3, 3, 4, 5, 1]))

#test4:
assert fifo(4, [1, 1, 1, 2, 2, 3]) == [1, 2, 3, -1] , "didn't pass the Test4: the result it has to be '[1, 2, 3, -1]' not {}".format(fifo(4, [1, 1, 1, 2, 2, 3]))

#test5:
assert fifo(1, [5, 4, 3, 3, 4, 10]) == [10] , "didn't pass the Test5: the result it has to be '[10]' not {}".format(fifo(1, [5, 4, 3, 3, 4, 10]))

#test6:
assert fifo(3, [1, 1, 1, 1, 1, 1, 1, 1]) == [1, -1, -1] , "didn't pass the Test6: the result it has to be '[1, -1, -1]' not {}".format(fifo(3, [1, 1, 1, 1, 1, 1, 1, 1]))

#test7:
assert fifo(5, [10, 9, 8, 7, 7, 8, 7, 6, 5, 4, 3, 4, 3, 4, 5, 6, 5]) == [5, 4, 3, 7, 6] , "didn't pass the Test7: the result it has to be '[5, 4, 3, 7, 6]' not {}".format(fifo(5, [10, 9, 8, 7, 7, 8, 7, 6, 5, 4, 3, 4, 3, 4, 5, 6, 5]))
print("Test Ok")
