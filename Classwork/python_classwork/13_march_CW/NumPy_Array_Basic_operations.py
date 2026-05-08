import numpy as np
#creating array
numbers1=np.array([45,78,90])
print ("array")
print(numbers1)
print("------------------")
print("------------------")
#second array
numbers2=np.array([45,3.5,90])
print("Array")
print(numbers2)
print("------------------")
print("------------------")
#third array
numbers3=np.array([45,3.5,90,'hello'])
print ("Array")
print(numbers3)
print("------------------")
print("------------------")
#multiply these elements by 3
print("After multiplying by 3:")
print(numbers1*3)
print("------------------")
print("------------------")
#elements greater than 70
print("Elements greater than 70")
print(numbers1>70)
print("------------------")
print("------------------")
#Double dimensionAL array
matrix1=np.array([[45,67,89],[56,90,78]])
print("2D MATRIX")
print(matrix1)
print("------------------")
print("------------------")
#3d array
array3d=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("3d array")
print(array3d)
print("------------------")
print("------------------")
#creating array
number5=np.array([45,67,89,4,34,])
print("Array :")
print(number5)
print("------------------")
print("------------------")
#multiplying each element by 10
print("After multiplying by 10")
print(number5*10)

'''output:

array
[45 78 90]
------------------
------------------
Array
[45.   3.5 90. ]
------------------
------------------
Array
['45' '3.5' '90' 'hello']
------------------
------------------
After multiplying by 3:
[135 234 270]
------------------
------------------
Elements greater than 70
[False  True  True]
------------------
------------------
2D MATRIX
[[45 67 89]
 [56 90 78]]
------------------
------------------
3d array
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
------------------
------------------
Array :
[45 67 89  4 34]
------------------
------------------
After multiplying by 10
[450 670 890  40 340]
'''

