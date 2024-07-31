Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:30:09) [MSC v.1934 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a =
SyntaxError: incomplete input
# operation and repetation
a = [12,14,16,18,20]
print(a)
[12, 14, 16, 18, 20]
b = a*2
b
[12, 14, 16, 18, 20, 12, 14, 16, 18, 20]

#concatenation
a= [1,2,3,4,5]
b= [6,7,8,9,10]
print(a+b)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#list methods
#append
 a =[1,2,3]
 
SyntaxError: unexpected indent
a.append(4)

a = [1,2,3]
a.append(4)
a
[1, 2, 3, 4]

#insert
a =[1,2,3]
a.insert(1,4)
a
[1, 4, 2, 3]
# extend
a =[1,2,3]
b =[4,5,6]
a.extend(b)
a
[1, 2, 3, 4, 5, 6]
#remove()
a = [1,2,3,2]
a.remove(2)
a
[1, 3, 2]
#index
a =[1,2,3]
b = a.index(3)
a
[1, 2, 3]

b
2
#count
a = [1,2,,3,2,2]
SyntaxError: invalid syntax


a = [1,2,3,2,3,2,2]
b = a.count(2)
b
4

#sort






































































































































































#sort
a = [1,2,4,5,6,7]
a.sort()
a
[1, 2, 4, 5, 6, 7]
 a = [7,4,,9,3,2,5]
 
SyntaxError: unexpected indent
a ={7,3,9,6,1]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'

a=[7,3,1,9,4,2]
a.sort()
>>> a
[1, 2, 3, 4, 7, 9]
>>> #reverse
>>> a =[1,2,3,4,5,6,7,8,9]
>>> a.reverse()
>>> a
[9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> #copy
>>> a = [1,2,3,4]
>>> b = a.copy()
>>> b
[1, 2, 3, 4]
>>> # clear
>>> a =[1,2,3,4,5,6]
>>> a.clear()
>>> a
[]
>>> #min
>>> a =[1,2,3,4,5,6,7,8,9]
>>> b =min(a)
>>> b
1
>>>  # max
...  
>>> a =[1,2,3,4,5,6,7,8,9]
>>> b=max()
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    b=max()
TypeError: max expected at least 1 argument, got 0
>>>  a =[1,2,3,4,5,6,7]
...  
SyntaxError: unexpected indent
>>> a =[1,2,3,4,5]
>>> b=max(a)
>>> b
5
>>> #pop
>>> a=[1,2,3,4,5,6,7,8,9]
>>> b=pop(3)
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    b=pop(3)
NameError: name 'pop' is not defined. Did you mean: 'pow'?
>>> b= a.pop(3)
>>> b
4
