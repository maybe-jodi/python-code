# Lab13Bst.py
# "Mean, Median and Mode" 
# This is the student, starting version of Lab 13B.
# NOTE: This lab is meant for students in CS1-HONORS.
#       Students in REGULAR CS1 will do Lab 13A.


from random import *


sum = "shadowed" 
# prevents the use of this built-in function


def heading():
   print()
   print("**")
   print("Lab 13B, Mean, Median and Mode")
   print("80 Point Version")
   print("By: Ainsley Hines") # Substitute your own name here.
   print("**")
   print("\n")


def buildArray():
   # Specifying a seed creates "pseudo random" numbers 
   # that are the same with every program execution.
   seed(100)
   for k in range(amount):
      numbers.append(randint(10,99))


def displayArray():
   print()
   print(numbers)
   print()


def computeMean():
   return 0


def computeMedian():
   return 0


# precondition: The <numbers> array has exactly 1 mode.
def computeMode():
   return 0



##########
#  MAIN  #
##########

heading()
numbers = []
amount = eval(input("How many numbers do you want to generate?  -->  "))
buildArray()
displayArray()
print("Mean:  ",computeMean())
print("Median:",computeMedian())
print("Mode:  ",computeMode())
