Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:30:09) [MSC v.1934 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = {1,2,1.5,1+3j, 'hello'}
print(a)
{1.5, 2, 1, (1+3j), 'hello'}
type(a)
<class 'set'>
a = set({1,2,3,4,5})
type(a)
<class 'set'>
a = set([1,2,3,4,5])
type(a)
<class 'set'>
s = {'a','b','c'}
print(s)
{'a', 'b', 'c'}
s = {'A','B','C','D'}
print(s)
{'A', 'C', 'B', 'D'}
type(a)
<class 'set'>
s[0]]
SyntaxError: unmatched ']'
s[0]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
s.add('G')
S
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    S
NameError: name 'S' is not defined. Did you mean: 's'?
s.update(['H','J','I'])
s
{'H', 'D', 'J', 'A', 'C', 'G', 'I', 'B'}
s.add('G')
s
{'H', 'D', 'J', 'A', 'C', 'G', 'I', 'B'}
s.discard
<built-in method discard of set object at 0x0367A958>
s
{'H', 'D', 'J', 'A', 'C', 'G', 'I', 'B'}
b ={'hello','hi','navya'}
b.discard('language')
b
{'hello', 'navya', 'hi'}
b.remove('language')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    b.remove('language')
KeyError: 'language'
b.remove('language')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    b.remove('language')
KeyError: 'language'

b.remove('langage')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    b.remove('langage')
KeyError: 'langage'
b.remove('language")
         
SyntaxError: incomplete input
b.remove('language')
         
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    b.remove('language')
KeyError: 'language'
b.remove('navya')
         
b
         
{'hello', 'hi'}
s = {'A','B','C','D'}
         
s.pop(2)
         
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s.pop(2)
TypeError: set.pop() takes no arguments (1 given)
s.pop()
         
'A'
s.pop()
         
'C'

 
a ={1,2,3,4}
         
b ={3,4,5,6}
         
print(a|b)
         
{1, 2, 3, 4, 5, 6}

#union
         
print(a.uninon(b))
         
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(a.uninon(b))
AttributeError: 'set' object has no attribute 'uninon'. Did you mean: 'union'?
print(a.union(b))
         
{1, 2, 3, 4, 5, 6}

a ={1,2,3,4}
         
b ={3,4,5,6}
         
c ={5,6,7,8}
         
print(a|B|c)
         
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print(a|B|c)
NameError: name 'B' is not defined. Did you mean: 'b'?
print(a|b|c)
         
{1, 2, 3, 4, 5, 6, 7, 8}
print(a.unino(b,c))
         
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print(a.unino(b,c))
AttributeError: 'set' object has no attribute 'unino'. Did you mean: 'union'?
print(a.union(b,c))
         
{1, 2, 3, 4, 5, 6, 7, 8}
#intersection
         
a ={1,2,3,4,5}
         
b ={3,4,5,6,7}
         
print(a&b)
         
{3, 4, 5}

a ={1,2,3,4,5}
         
b ={3,4,5,6,7}
         
c ={5,6,7,8,9}
         
ptint(a&b&c)
         
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    ptint(a&b&c)
NameError: name 'ptint' is not defined. Did you mean: 'print'?
print(a&b&c)
         
{5}
print(a.interscetion(b,c))
         
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print(a.interscetion(b,c))
AttributeError: 'set' object has no attribute 'interscetion'. Did you mean: 'intersection'?
print(a.intersection(b))
         
{3, 4, 5}
print(a.intersection(b,c))
         
{5}
print(a.intersection update(b))
         
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a ={1,2,3,4,5}
         
b ={3,4,5,6,7}
         
print(a.imtersection(b))
         
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    print(a.imtersection(b))
AttributeError: 'set' object has no attribute 'imtersection'. Did you mean: 'intersection'?
print(a.intersection(b))
         
{3, 4, 5}
print(a)
         
{1, 2, 3, 4, 5}
print(b)
         
{3, 4, 5, 6, 7}
print(a.intersection_update(b))
         
None
(a.intersection_update(b))
         
a
         
{3, 4, 5}
print(a)
         
{3, 4, 5}
(b.intersection_update(a))
         
b
         
{3, 4, 5}
#difference
         
a =1[1,2,3,4}
         
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a ={1,2,3,4}
         
b ={2,3,4,5}
         
print(a-b)
         
{1}
a-b
         
{1}
a ={1,2,3,4}
         
b ={1,2,5,6}
         
a-b
         
{3, 4}
# symmetric difference
         
a ={1,2,3,4}
         
b ={1,2,5,6}
         
a^b
         
{3, 4, 5, 6}
print(a^b)
         
{3, 4, 5, 6}
print(a.symmetric_difference(b))
         
{3, 4, 5, 6}

#set
         
a = {1,2,3,4}
         
b = {1,2,4,5}
         
set(b)
         
{1, 2, 4, 5}
set(a)
         
{1, 2, 3, 4}
print(a.set(b))
         
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    print(a.set(b))
AttributeError: 'set' object has no attribute 'set'
a.set(b)
         
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    a.set(b)
AttributeError: 'set' object has no attribute 'set'
a
         
{1, 2, 3, 4}
b = a
         
a
         
{1, 2, 3, 4}
b
         
{1, 2, 3, 4}
 a.set(a)
         
SyntaxError: unexpected indent
a.set(a)
         
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    a.set(a)
AttributeError: 'set' object has no attribute 'set'
print(A.set(a))
         
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    print(A.set(a))
NameError: name 'A' is not defined. Did you mean: 'a'?
print(a.set(a))
         
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    print(a.set(a))
AttributeError: 'set' object has no attribute 'set'
a.add(4)
         
a
         
{1, 2, 3, 4}
a.update(8)
         
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    a.update(8)
TypeError: 'int' object is not iterable
a.update(4)
         
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    a.update(4)
TypeError: 'int' object is not iterable
a.update(3)
         
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    a.update(3)
TypeError: 'int' object is not iterable
a.clear()
         
a
         
set()
a = {}
         
type(a)
         
<class 'dict'>
a = set()
         
type(a)
         
<class 'set'>
 a ={1,2,3}
         
SyntaxError: unexpected indent
a ={1,2,3,4}
         
b =a.copy()
         
b
         
{1, 2, 3, 4}
a = {1,2,3,4}
         
b ={2,3,4,5}
         
a-b
         
{1}
a.difference(b)
         
{1}
a.differenece_update(b)
         
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    a.differenece_update(b)
AttributeError: 'set' object has no attribute 'differenece_update'. Did you mean: 'difference_update'?
>>> a.difference_update(b)
...          
>>> a
...          
{1}
>>> print(a)
...          
{1}
>>> a.difference_update(b)
...          
>>> print(a)
...          
{1}
>>> a ={1,2,3}
...          
>>> b ={2,3,4}
...          
>>> print(a)
...          
{1, 2, 3}
>>> a.difference(b)
...          
{1}
>>> a.difference_update(b)
...          
>>> a
...          
{1}
>>> print(a)
...          
{1}
>>> a.difference(b)
...          
{1}
>>> a.difference_update(b)
...          
>>> a
...          
{1}
>>> 
>>> #isdisjoint: checks if two sets arw disjoint(have no common elements)
...          
>>> a ={1,2,3}
...          
>>> b ={5,6,7}
...          
c =a.isdisjoint(b)
         
a
         
{1, 2, 3}
c
         
True

a= {1,2,3,4,5}
         
b ={2,3,4,5,6}
         
c =a.disjoint(b)
         
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    c =a.disjoint(b)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
c=a.isdisjoint(b)
         
a
         
{1, 2, 3, 4, 5}
#subset
         
a= {1,2}
         
b ={1,2,3,4}
         
c =a.issubset(b)
         
c
         
True
a={1,2,3}
         
b={4,5,6,7}
         
c=a.issubset(b)
         
c
         
False
