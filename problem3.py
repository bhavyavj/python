>>> adhoc = [1,2,3,1,4,5,66,22,2,6,0,9]
>>> for i in adhoc:
	if i>5:
		print(i)

		
66
22
6
9
>>> for i in adhoc:
	if i<=2:

		print(i)

		
1
2
1
2
0
>>> a = [ i for i in adhoc   if i<=2]
>>> 
>>> 
>>> 
>>> print(a)
[1, 2, 1, 2, 0]
>>> b = [i for i in adhoc    if i>5]
>>> print(b)
[66, 22, 6, 9]
