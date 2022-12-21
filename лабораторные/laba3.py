# задание 1
numbers = []
for i in range(1,11):
    for i in input('Введите число ').split():
        numbers.append(int(i))
print(numbers)
print(sum(numbers))

# задание 2
numbers = []
for i in range(1, 11):
    for i in input('Введите число ').split():
        numbers.append(int(i))
        num_of_0 = numbers.count(0)
print(num_of_0)

# задание 3
n = int(input('Введите натуральное число: '))
les = ''
for i in range(1, n+1):    
    les = les + str(i)
    print(les)

# задание 4
n = int(input('Введите любое натуральное число: '))
for i in range(1,n+1):
    for a in range(1, n+1-i):
        print('', end=' ')
    for b in range (1,i+1):
        print(b, end= '')
    for c in range(i-1,0,-1):
        print(c, end = '')
    print()
