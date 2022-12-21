# задание 1
v='#1'
a= True
b= False
print(v, a and b)

v='#2'
print(v,(a and b) or b)

v='#3'
print(v,(a and b) or not (a and b))

v='#4'
print(v,a and b or not(a or b) or b)

v='#5'
print(v, b and b or not a and(a or b or a) or not(a or b))

v='#6'
print(v, 1<<2)

v='#7'
print(v, 1 & 0 | 1>>1)

v='#8'
print(v, 1 & 0| 1>>0)

v='#9'
print(v, 0b101 & 0b111 ^ 0b111 | 0b010)

# задание 2
a=int(input('Наберите число 1: '))
b=int(input('Наберите число 2: '))
print(min(a, b))

# задание 3 
a=int(input('Введите 1 число: '))
b=int(input('Введите 2 число: '))
c=int(input('Введите 3 число: '))
print(max(a, b ,c))

# задание 4
a=int(input('Введите 1 число: '))
b=int(input('Введите 2 число: '))
c=int(input('Введите 3 число: '))
lst = [a, b, c]
print(len(set(lst)))
