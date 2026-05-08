import numpy as np
#reshape example

arrayy1=np.array([32,56,78,90,56,45,89,12])
print("First Array:")
print(arrayy1)
print("------------------------------------------------------------")
#reshaping in order 4,2
arrayy2=arrayy1.reshape(4,2)

print(arrayy2)
print("------------------------------------------------------------")
# reshaping in 3d array 
arrayy4=arrayy1.reshape(2,2,2)
print("First reshaped array")
print(arrayy4)

print("------------------------------------------------------------")
arrayy5=arrayy1.reshape(2,4,1)
print("second reshaped array")
print(arrayy5)

print("------------------------------------------------------------")
arrayy6=arrayy1.reshape(8,1,1)
print("third reshaped array")
print(arrayy6)

print("------------------------------------------------------------")
arrayy7=arrayy1.reshape(1,4,2)
print("fourth reshaped array")
print(arrayy7)

print("------------------------------------------------------------")
arrayy8=arrayy1.reshape(1,1,8)
print("fifth reshaped array")
print(arrayy8)

print("------------------------------------------------------------")
arrayy9=arrayy1.reshape(2,1,4)
print("sixth reshaped array")
print(arrayy9)

print("------------------------------------------------------------")
arrayy10=arrayy1.reshape(1,2,4)
print("Seventh reshaped array")
print(arrayy10)

print("------------------------------------------------------------")
arrayy11=arrayy1.reshape(4,2,1)
print("Eighth reshaped array")
print(arrayy11)


'''output:
First Array:
[32 56 78 90 56 45 89 12]
------------------------------------------------------------
[[32 56]
 [78 90]
 [56 45]
 [89 12]]
------------------------------------------------------------
First reshaped array
[[[32 56]
  [78 90]]

 [[56 45]
  [89 12]]]
------------------------------------------------------------
second reshaped array
[[[32]
  [56]
  [78]
  [90]]

 [[56]
  [45]
  [89]
  [12]]]
------------------------------------------------------------
third reshaped array
[[[32]]

 [[56]]

 [[78]]

 [[90]]

 [[56]]

 [[45]]

 [[89]]

 [[12]]]
------------------------------------------------------------
fourth reshaped array
[[[32 56]
  [78 90]
  [56 45]
  [89 12]]]
------------------------------------------------------------
fifth reshaped array
[[[32 56 78 90 56 45 89 12]]]
------------------------------------------------------------
sixth reshaped array
[[[32 56 78 90]]

 [[56 45 89 12]]]
------------------------------------------------------------
Seventh reshaped array
[[[32 56 78 90]
  [56 45 89 12]]]
------------------------------------------------------------
Eighth reshaped array
[[[32]
  [56]]

 [[78]
  [90]]

 [[56]
  [45]]

 [[89]
  [12]]]


'''
