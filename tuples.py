Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:30:09) [MSC v.1934 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = (10, 'hello',10.5, 1+3j)
a
(10, 'hello', 10.5, (1+3j))
print(a)
(10, 'hello', 10.5, (1+3j))
print(type(a))
<class 'tuple'>
a = ('hello')
a
'hello'
type(a)
<class 'str'>
a =( 'hello',)
a
('hello',)
type(A)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    type(A)
NameError: name 'A' is not defined. Did you mean: 'a'?
type(a)
<class 'tuple'>
 a= 10,10.3,'hello'
 
SyntaxError: unexpected indent
a =10,10.3,1+3j,'hello'
a
(10, 10.3, (1+3j), 'hello')
type(a)
<class 'tuple'>

a =[10]
type(a)
<class 'list'>
a =[10,23]
type(a)
<class 'list'>

a(0)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a(0)
TypeError: 'list' object is not callable
a = [10,34.2,'hello,1+3j']
a
[10, 34.2, 'hello,1+3j']
a[0]
10

a = (10,34.2,'hello,1+3j')

a =(10,1.2,'hello',1+3j,[10,2,10.3])
a
(10, 1.2, 'hello', (1+3j), [10, 2, 10.3])
a(4)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a(4)
TypeError: 'tuple' object is not callable
a[4]
[10, 2, 10.3]
a[4][0]
10
a[4][2]
10.3
a[-1]
[10, 2, 10.3]
a[-2]
(1+3j)

a = (10, 'hello', 10.5,1+3j,,[10,3,2.3],(1,3.2,1+3j))
SyntaxError: invalid syntax
type(a)
<class 'tuple'>
s = ([10,'hello'])
type(s)
<class 'list'>
s = ([10,'hello'])
type(a)
<class 'tuple'>
a
(10, 1.2, 'hello', (1+3j), [10, 2, 10.3])
 g =[(10,3.4,'navya')]
 
SyntaxError: unexpected indent
g =[(10,3.4,'navya')]
type(a)
<class 'tuple'>
a[-4:-1]
(1.2, 'hello', (1+3j))
a[1:2]
(1.2,)
g[1:4]
[]
g[1:2]
[]
a[0:6:2]
(10, 'hello', [10, 2, 10.3])
a[0:6:-2]
()
a[-5:-1:2]
(10, 'hello')
a[0:5]]
SyntaxError: unmatched ']'
a[0:5]
(10, 1.2, 'hello', (1+3j), [10, 2, 10.3])
a [10,10.4,'hello']
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a [10,10.4,'hello']
TypeError: tuple indices must be integers or slices, not tuple
a[10,10.2,'hello']
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a[10,10.2,'hello']
TypeError: tuple indices must be integers or slices, not tuple

 a[10,10.2,'hello']
 
SyntaxError: unexpected indent
a[10,10.2,'hello']
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a[10,10.2,'hello']
TypeError: tuple indices must be integers or slices, not tuple


a =[10,10.5,'hello']
a
[10, 10.5, 'hello']
type(a)
<class 'list'>
a[2]
'hello'
del a(2)
SyntaxError: incomplete input
del a[2]

type(a)
<class 'list'>
 a =(10,10.3, 'hello')
 
SyntaxError: unexpected indent
a =(10,10.3,'navya')
type(a)
<class 'tuple'>
a[2]
'navya'
del a(2)
SyntaxError: incomplete input
del a[2]
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    del a[2]
TypeError: 'tuple' object doesn't support item deletion
del a(2)
SyntaxError: incomplete input
del a(2)
SyntaxError: incomplete input
 a =('python', 15.38,25)
 
SyntaxError: unexpected indent
b =('hello',23.23,15)

a[10,10.2,'hello']
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    a[10,10.2,'hello']
TypeError: tuple indices must be integers or slices, not tuple
b =('hello',23.23,15
    a =('python', 15.38,25)
    
SyntaxError: '(' was never closed


a =('python',10,10.2)
    
b =('hello',10,10.3)
    
print(a*3)
    
('python', 10, 10.2, 'python', 10, 10.2, 'python', 10, 10.2)
print(a+b)
    
('python', 10, 10.2, 'hello', 10, 10.3)


#tuple methods
    
 a=(1,2,3,'hello')
    
SyntaxError: unexpected indent
a = (1,2,3,'hello')
    

a = (1,2,3,'hello')
    
a
    
(1, 2, 3, 'hello')
len(a)
    
4
a = (1,2,3,'hello')
    
b = a.count(2)
    
b
    
1
a = (1,2,3,'hello',2,2,3,4,5,6,7,7,7,7,7)
    
b = count.a(7)
    
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    b = count.a(7)
NameError: name 'count' is not defined. Did you mean: 'round'?
b
    
1
a.count (7)
    
5
 b =a.index('hello')
    
SyntaxError: unexpected indent
b = a.index('hello')
    
b
    
3
a = (1,2,3)
    
b = a+(4+5)
    
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    b = a+(4+5)
TypeError: can only concatenate tuple (not "int") to tuple
b = a+(4,5)
    
b
    
(1, 2, 3, 4, 5)

 a =(1,2,3,4,5,6,7,8)
    
SyntaxError: unexpected indent
a =(1,2,3,4)
    
a
    
(1, 2, 3, 4)
a =min()
    
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    a =min()
TypeError: min expected at least 1 argument, got 0
 a =(1,2,3,4,5,6)
    
SyntaxError: unexpected indent
a =(1,2,3,4,5,6,7)
    
b = min(a)
    
b
    
1
c =max(a)
    
c
    
7
 a =[1,2,3,4,5,6]
    
SyntaxError: unexpected indent
a =[1,2,3,5,5,6]
    
type(a)
    
<class 'list'>
a.reverse()
    
a
    
[6, 5, 5, 3, 2, 1]
type(a)
    
<class 'list'>
 a =(1,2,3,4,5)
    
SyntaxError: unexpected indent
a =(1,2,3,5,5)
    
type(a)
    
<class 'tuple'>
a.reverse()
    
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    a.reverse()
AttributeError: 'tuple' object has no attribute 'reverse'
a.reverse()
    
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    a.reverse()
AttributeError: 'tuple' object has no attribute 'reverse'
a[::-1]
    
(5, 5, 3, 2, 1)
>>>  a = (1,2,3,4,5)
...     
SyntaxError: unexpected indent
>>> a = (1,2,3,4)
...     
>>> a = (1,2,3,5,6)
...     
>>> type(a)
...     
<class 'tuple'>
>>> b =list(a)
...     
>>> b
...     
[1, 2, 3, 5, 6]
>>> b.reverse()
...     
>>> b
...     
[6, 5, 3, 2, 1]
>>> type(a)
...     
<class 'tuple'>
>>> c = str(a)
...     
>>> c
...     
'(1, 2, 3, 5, 6)'
>>> type(c)
...     
<class 'str'>
>>> b =(1,2,3,4)
...     
>>> b
...     
(1, 2, 3, 4)
>>> type(b)
...     
<class 'tuple'>
>>> b =list(a)
...     
>>> b
...     
[1, 2, 3, 5, 6]
>>> type(b)
...     
<class 'list'>
