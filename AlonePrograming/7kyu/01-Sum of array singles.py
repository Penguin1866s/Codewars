def repeats(arr):
    num_repts = []
    for i in arr:
        if arr.count(i) == 1:
            num_repts.append(i)
        else:
            continue
    return sum(num_repts)

print(repeats([4,5,7,5,4,8]))