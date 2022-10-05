def merge(first, second):
    f_arr = []
    l1 = 0
    l2 = 0
    while (l1 < len(first)) and (l2 < len(second)):
        if first[l1] < second[l2]:
            f_arr.append(first[l1])
            l1 += 1
        else:
            f_arr.append(second[l2])
            l2 += 1
    if l2 < len(second):
        while l2 < len(second):
            f_arr.append(second[l2])
            l2 += 1
    else:
        while l2 < len(first):
            f_arr.append(first[l1])
            l1 += 1
    return f_arr