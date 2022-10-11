# Array

+ [Diagonal Sum in arrays](#diagonal_sum_in_arrays)
+ [Merge of sorted arrays](#merge_of_sorted_arrays)
+ [Squares in arrays](#squares_in_arrays)
+ [Compress](#compress)
## Diagonal Sum in arrays

```python 
def diagonalSum(mat):
    sum = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i == j or (i + j + 1) == len(mat):
                sum += mat[i][j]
    return sum
```    


## Merge of sorted arrays

```python 
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
```
    
## Squares in arrays

```python 
def squares(s):

    i = 0
    while (i < len(s) and s[i] < 0):
        i += 1
    s1 = [s[cur] ** 2 for cur in range(i - 1 , -1, -1)]
    s2 = [s[cur] ** 2 for cur in range(i, len(s))]

    return merge(s1, s2)
```

## Compress

```python 
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
  ```
