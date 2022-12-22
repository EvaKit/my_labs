# задание 1
any_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []
def odd_index(list):
    for i in range(len(list)):
        if i % 2 == 0:
            result.append(list[i])
    print(result)
odd_index(any_list)

# задание 2
any_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []
def more(list):
    for i in range(len(list)):
        if list[i] > list[i - 1]:
            result.append(list[i])
    print(result)
more(any_list)

# задание 3
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def replace(list):
    max_ = list.index(max(list))
    min_ = list.index(min(list))
    list[max_], list[min_] = list[min_], list[max_]
    print(list)
replace(list_a)

# задание 4
a = {1: 'Левая палочка твикс', 2: 'Правая палочка твикс' }
key = int(input('Набери 1 или 2 и узнай на чьей стороне ты'))
def get_value(dictionary):
    value = dictionary.get(key)
    print(value)
get_value(a)

# задание 5
from figures import triangle_area
triangle_area()
