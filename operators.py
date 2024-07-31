Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:30:09) [MSC v.1934 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 4
b = 6
a<b and a>b
False
a<b and a<b
True
a>b and a<b
False
>>> a>b and a>b
False
>>> 
>>> # OR operator
>>> a<b or a>b
True
>>> a>b or a>b
False
>>> not a<b
False
>>> not a>b
True
>>> #bitwise operator
>>> a = 20
>>> b = 4
>>> a & b
4
>>> a =40
>>> b =2
>>> a&b
0
>>> #or operator
>>> a = 20
>>> b = 4
>>> a/b
5.0
>>> a|b
20
>>> a =40
>>> b = 2

>>> a|b
42
>>> a +20
60
>>> a = 20
>>> a<<2
80
>>> a>>2
5
>>> a = 10
>>> ~a
-11
>>> a =20
>>> b = 2
>>> a^b
22
