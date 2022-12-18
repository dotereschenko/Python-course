# comprehension, filter, map


+ [Task 1](#task-1)
+ [Task 2](#task-2)
+ [Task 3](#task-3)
+ [Task 4](#task-4)
+ [Task 5](#task-5)
+ [Task 6](#task-6)
+ [Task 7](#task-7)
+ [Task 8](#task-8)
+ [Task 9](#task-9)
+ [Task 10](#task-10)
+ [Task 11](#task-11)
+ [Task 12](#task-12)
+ [Task 13](#task-13)
+ [Task 14](#task-14)
+ [Task 15](#task-15)
+ [Task 16](#task-16)

<!---delimeter--->

## Task 1

Найти все числа от 1 до 1000, которые делятся на 17.

```python
arr1 = [i for i in range(1,1001) if i % 17 == 0]
print(arr1, end="\n")
```

## Task 2
Найти все числа от 1 до 1000, которые содержат в себе цифру 2.

```python
arr2 = [i for i in range(1,1001) if '2' in str(i)]
print(arr2)

```

## Task 3
Найти все числа от 1 до 10000, которые являются палиндромом.

```python
arr3 = [i for i in range(1,10001) if str(i) == str(i)[::-1]]
print(arr3)

```

## Task 4
Посчитать количество пробелов в строке.

```python
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
print(len(string)-len("".join([char for char in string if char not in " "])))

```

## Task 5
Есть любая последовательность непробельных символов латинского алфавита, удалить все гласные из этого слова.

```python
string1 = "ASDSDJFIDDIOXCOScsdvfdcasewfqffevsv543"
print("".join([char for char in string1 if char not in "aeiouAEIOU"]))

```

## Task 6
На входе строка со словами, разделенными через 1 пробел. Найти все слова, длина которых не больше 5.

```python
string2 = "fwesddf ewdfd3 fefeff 3r4r2 efsdf"
print(len([i for i in string2.split() if len(i) == 5]))

```

## Task 7
На входе строка со словами, разделенными через 1 пробел. Получить словарь, где в качестве ключа используется само слово, а в значении длина этого слова.

```python
print({i: len(i) for i in string.split()})

```

## Task 8
На входе предложение со всеми пробельными и непробельными символами латинского алфавита. Получить словарь используемых букв в строке, то есть на выходе список уникальных букв.

```python
print({i for i in list(string)})

```

## Task 9
На входе список чисел, получить список квадратов этих чисел / use map.

```python
arr4 = [1,2,3,4,5,6]
print([i**2 for i in arr4])

```

## Task 10
На входе список координат, например, [(1, 1), (2, 3), (5, 3)]. Найти все точки, которые принадлежат прямой y = 5 * x - 2. 
На выходе получить словарь из самой точки и расстоянии до этой точки из начала координат (0, 0).

```python
import math
arr5 = [(1,2),(4,6),(4,4),(8,3)]
print({(x,y): math.sqrt(x**2+y**2) for (x,y) in arr5})

```

## Task 11
Возвести в квадрат все четные числа от 2 до 27. На выходе список.

```python
arr6 = [i**2 for i in range(2,27) if i%2==0]
print(arr6)

```

## Task 12
На входе список из координат точек на плоскости. Найти расстояние до самой удаленной точку от начала координат (0, 0) в первой четверти.

```python
arr7 = [(1,2),(3,6),(6,4),(123,-6),(12,-12)]
print(max([math.sqrt(x**2+y**2) for (x,y) in arr7 if x>0 and y>0]))

```

## Task 13
На входе два списка чисел nums_first = [1, 2, 3, 5, 8] и nums_second = [2, 4, 8, 16, 32]. Получить пары сумм и разниц, [(3, -1), (6, -2), (11, -5), ...].

```python
nums_first = [1, 2, 3, 5, 8]
nums_second = [2, 4, 8, 16, 32]
print([(x + y,x-y) for x, y in zip(nums_first, nums_second)])

```

## Task 14
На входе список строк из чисел, например, ['43141', '32441', '431', '4154', '43121']. Найти четные квадраты этих чисел. Ответ записать снова в список из строк, то есть сформировать обратно список строк, но уже отфильтровать все четные квадраты.


```python
arr8 = ['43141', '32441', '431', '4154', '43121']
print([i for i in arr8 if (int(i)**2) % 2 == 0])

```

## Task 15
Менеджер как обычно придумал свое представление данных, а нам оно не подходит.

input_str = """name,Petya,Vasya,Masha,Vova
grade,5,5,8,3
subject,math,language,physics,math
year,1999,2000,1995,1998"""


Мы хотим получить нормальную таблицу, чтобы импортировать в csv.

```python
input_str = """name,Petya,Vasya,Masha,Vova
grade,5,5,8,3
subject,math,language,physics,math
year,1999,2000,1995,1998"""
import json
d = {x.split(",")[0]:x.split(",")[1::] for x in input_str.split()}
print(json.dumps([{j: d[j][k] for j in d.keys()} for k in range(len(d.keys()))],indent=2))

```

## Task 16
Получить сумму по столбцам у двумерного списка.

```python
a = [[11.9, 12.2, 12.9],
     [15.3, 15.1, 15.1],
     [16.3, 16.5, 16.5],
     [17.7, 17.5, 18.1]]
print(a)
print(*a)
print([sum(x) for x in zip(*a)])

```
