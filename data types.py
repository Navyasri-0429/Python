Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:30:09) [MSC v.1934 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 5
print(a)
5
print(type(a))
<class 'int'>
b = 30.4
print(type(b))
<class 'float'>
c = 1+3j
print(type(a))
<class 'int'>
a =  "Hello"
print(type(a))
<class 'str'>
a = ''' this is navya'''
print(a)
 this is navya
print(type(a))
<class 'str'>
a = NAVYA
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a = NAVYA
NameError: name 'NAVYA' is not defined
a = 'NAVYA'
a(2)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a(2)
TypeError: 'str' object is not callable
a(2)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a(2)
TypeError: 'str' object is not callable
a[2]
'V'
'V'
'V'
a[1]
'A'
'A'
'A'
a = 'HELLO'
a[0:5]
'HELLO'
a[1;4]
SyntaxError: invalid syntax
a[1:4]
'ELL'
a[0:9]
'HELLO'
a[1:4]
'ELL'

a[-4]
'E'
>>> a[-1]
'O'
>>> a[-5:-1]
'HELL'
>>> a[-5:0]]
SyntaxError: unmatched ']'
>>> a[-5:-3]
'HE'
>>> a[-5]
'H'
>>> a[:-1]
'HELL'
>>> a[-5:]
'HELLO'
>>> a[-5:-6]
''
>>> a[-7:-5]
''
>>> a[-2-:2]
SyntaxError: invalid syntax
>>> a[-2:-1]
'L'
>>> a = REFRIGIRATOR
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a = REFRIGIRATOR
NameError: name 'REFRIGIRATOR' is not defined
>>> a = 'REFRIGIRATOR'
>>> a[0:12:5]
'RGO'
>>> a[0:12:3]
'RRIT'
>>> a[0:12:12]
'R'
>>> a[0:12:1]
'REFRIGIRATOR'
>>> a[-1:-12:-2]
'RTRGRE'
>>> a[-1:-12:-3]
'RAGF'
>>> a[-12::2}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a[-12::2]
'RFIIAO'
>>> a = 'REFRIGERATOR'
>>> a[-12::4]
'RIA'
