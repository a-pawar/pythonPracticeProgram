
i=8
print(type(i))
#<class 'int'>
j=1.4
print(type(j))
#<class 'float'>
k='anshul'
print(type(k))
#<class 'str'>
#string(i)
'''
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    string(i)
NameError: name 'string' is not defined
'''
j=int(j)
print(j)
1
i=float(i)
print(i)
8.0
i=str(i)
print(i)
'8.0'
print(type(i))
#<class 'int'>
i=float(i)
print(i)
8.0
print(type(i))
#<class 'float'>
#k=int(k)
'''
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    k=int(k)
ValueError: invalid literal for int() with base 10: 'anshul'
'''
a=1+3j
print(a)
(1+3j)
print(type(a))
#<class 'complex'>
b=1+j6
'''
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    b=1+j6
NameError: name 'j6' is not defined. Did you mean: 'j'?
'''

