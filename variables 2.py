Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:30:09) [MSC v.1934 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=a=v=y=a=29
>>> a
29
>>> a
29
>>> v
29
>>> a,b,c = 1,2,3
>>> a
1
>>> c
3
>>> a = 29
>>> del(a)
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> 
>>> nameOfthestudent = "navya"
>>> Nameofthestudent ="amrutha"
>>> name_of_the_student ="likhitha"
>>> #comment
>>> a = 10 #assigning value 10 to the variable a
>>> print(a)
10
>>> 
>>> #Python Keywords
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> a = Keyword.kwlist
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a = Keyword.kwlist
NameError: name 'Keyword' is not defined. Did you mean: 'keyword'?
>>> a = keyword.kwlist
>>> len(a)
35
