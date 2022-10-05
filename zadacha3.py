def merge(s, l):
    arr = list()
    pl = 1
    pr = 0
    left = s[:l]  
    right = s[l:] 
    print(left, right)
    while len(left) + 1 > pl and len(right) > pr:
        if abs(left[-pl]) <= right[pr]:
            arr.append(abs(left[-pl]) ** 2)
            pl += 1
        else:
            arr.append(right[pr] ** 2)
            pr += 1
    while len(left) + 1 > pl:
        arr.append(abs(left[-pl]) ** 2)
        pl += 1
    while len(right) > pr:
        arr.append(right[pr] ** 2)
        pr += 1
    return arr
   
def check(mid):
    if s[mid] > 0:
        return True
    else:
        return False
    pass


def main():
    for i in range(len(s)):
        l = 0
        r = len(s)
        while l < r:
            mid = (l + r) // 2
            if check(mid):  # if positive
                r = mid - 1
            else:
                l = mid + 1
    print(l)
    return merge(s, l)


if __name__ == '__main__':
    print(main())