def compress(arr):
    
    arr.append(None)
    pr = arr[0]
    count = 1
    Arr1 = []
    
    for i in range(1,len(arr)):
        if arr[I] != prev:
            if count != 1:
                arr1.append(f"{prev}{count}")
            else:
                arr1.append(f"{prev}")
            prev = arr[i]
            count = 1
        else:
            count += 1
            
    return ''.join(arr1)