""" Python code to convert one data type to another data type """

num = '123'
print(type(num).__name__)

num = int(num)
print(num, type(num).__name__)

n = 123.23
print(type(n).__name__)
n = int(n)
print(n, type(n).__name__)

t = True
print(type(t).__name__)
t = int(t)
print(t, type(t).__name__)