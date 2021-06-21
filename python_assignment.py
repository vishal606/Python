#!/usr/bin/env python
# coding: utf-8

# # Python Programing Assignment

# Name : Bishal Paul
# 

# ID : 17-35836-3 

# # Problem - 1 

# * Two list and concatenate

# In[60]:


list1 = ["py", "i", "m", "favou", "lang"]
list2 = ["thon", "s", "y", "rite", "uage"]
list_concate = ''.join([list1[0]+ list2[0] + ", "] + [list1[1] + list2[1] + ", "] + [list1[2]+ list2[2] + ", "] + [list1[3] + list2[3] + ", "] + [list1[4] + list2[4]])
print(list_concate)


# # Problem - 2

# * NumPy array create another array which contains the odd rows and even colum

# In[63]:


import numpy
arr = numpy.array([[20 ,66, 88, 12], 
                   [75 ,19, 92, 71], 
                   [27 ,90, 33, 67], 
                   [21 ,14, 25, 38], 
                   [51 ,44, 57, 77]])
arr[::2]   
arr[:, 1::2]
arr[::2, 1::2]


# # Problem - 3

# * Create an 8x3 NumPy integer array from a range between 10 to 34 (using numpy.arange() function) such that the difference betweeneach element is 1 and then Split the array into 4 (four) equal-sized sub-arrays.

# In[49]:


import numpy

print("Creating 8X3 array using numpy\n")
sampleArray = numpy.arange(10, 34, 1)
sampleArray = sampleArray.reshape(8,3)
print (sampleArray)

print("\nDividing 8X3 array into 4 sub array\n")
subArrays = numpy.split(sampleArray, 4) 
print(subArrays)


# # Problem - 4

# * Create a 3x3 NumPy integer array

# In[50]:


import numpy

print("Printing Original array")
Orginal_Array = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
print (Orginal_Array)

sort_By_Row = Orginal_Array[:,Orginal_Array[1,:].argsort()]
print("Sorting Original array by secoond row")
print(sort_By_Row)

print("Sorting Original array by secoond column")
sort_By_Column = Orginal_Array[Orginal_Array[:,1].argsort()]
print(sort_By_Column)


# # Problem - 5

# In[61]:


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    pass
class Mini_Bus(Bus):
    pass

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())


# # Problem - 6

# * Create a dictionary which contains all the reserved keywords and their meanings in Python programming languag. Also, create a functionto check wheter a given word (taken from user) is reserved keyword or not.

# In[144]:


import keyword
def isKeyword(word) :
    keyword_list = keyword.kwlist
    if word in keyword_list :
       return "Yes"
    else :
      return "No"
if __name__ == '__main__':
	s = input("Enter a Keyword : ")
	iskey = keyword.iskeyword(s)
	print(s,'Keyword is :',iskey)


# # Problem - 7
# 

# * A sample pattern of Pascal Triange, which contains 7 rows:

# In[55]:


def printPascal(n) :
    
    for line in range(0, n) :   
        for i in range(0, line + 1) :
            print(binomialCoeff(line, i),
                " ", end = "")
        print()

def binomialCoeff(n, k) :
    res = 1
    if (k > n - k) :
        k = n - k
    for i in range(0 , k) :
        res = res * (n - i)
        res = res // (i + 1)
     
    return res

n = 7
printPascal(n)

