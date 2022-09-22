from array import *

# MAKING  2D ARRAY AND GIVING SOME SIZE FROM USER  INPUT
myArray = []
arraySize = int(input("ENTER SIZE  OF ARRAY : "))

# TAKING INPUT FRM USER --- SIZE IS THE NUMBER OF ROWS AND  COLUMNS (3X3 ARRAY )
print("ENTER %d  ELEMENTS IN A ROW " % arraySize)
for x in range(arraySize):
    myArray.append([int(y) for y in input().split()])
print(myArray)

# UPDATING ELEMENTS OF THE 2 DIMENSIONAL - ARRAY

myArray[0] = [69, 420]

myArray[2] = [420, 69]
print("UPDATING 2nd INDEX OF ARRAY : ")
print(myArray)
print("UPDATING 0th INDEX OF ARRAY : ", myArray)

print("-----------------------------------------")

# TRAVERSING WITH 2D ARRAYS

print("TRAVERSING AN ARRAY ")
newArray = [[1, 1, 1, 1], [2, 3, 4, 5], [3, 4, 5, 6]]
print("CURRENT ARRAY IS : ", newArray)
for x in newArray:
    for y in x:
        print(y, end=" ")
    print()
print("-------------------------------------------")

# DELETING  ELEMENTS  FROM ARRAYS

delArray = [[5, 5, 5, 5], [2, 9, 7, 6], [4, 4, 4, 4]]
print("ARRAY BEFORE DELETION OF ELEMENTS : ")
print(delArray)

print("DELETING THE 1st INDEX : ")
del (delArray[1][0])

print("ARRAY AFTER DELETING THE 1st and 2nd INDEX :  ")
del (delArray[1])

for x in delArray:
    for y in x:
        print(y, end=" ")
    print()

print("---------------------------")

# SLICING ARRAYS AND/OR FINDING ITS LENGTH

sliceArr = [[1, 2, 3, 4], [7, 5, 8, 9], [4, 5, 6, 7]]

slice1 = sliceArr[1:3]
slice2 = sliceArr[:1]

print("\nTHE CURRENT ARRAY IS : ", sliceArr)
print("\nTHE ARRAY AFTER SLICING 1st INDEX  : ", slice1)
print("\nTHE ARRAY AFTER SLICING 1st INDEX : ", slice2)

print("\n THE LENGTH OF THE ARRAY IS  : ", len(sliceArr))

print("------------------------------")


# TIME COMPLEXITY : AMOUNT OF TIME TAKEN BY COMPUTER TO RUN AN ALGORITHM

# STACK  : WORKS ON PRINCIPLE OF LIFO (LAST IN - FIRST OUT )
# MAKING THE STACK AS A LIST

def create_stack():
    stack = []
    return stack


def checkEmpty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print("PUSHED ITEM IS : " + item)


def pop(stack):
    if (checkEmpty(stack)):
        return "STACK IS EMPTY"
    else:
        return stack.pop()


# PUSH : USED TO ADD ELEMENT IN THE STACK
# POP  : USED TO REMOVE THE TOP MOST  ELEMENT OF THE STACK
# PEEK : USED TO DISPLAY THE TOP-MOST VALUE OF THE STACK

stack = create_stack()
push(stack, str(6))
push(stack, str(9))
pop(stack)
print(stack)

# ---------------------------

# STACKS ARE USED IN THE BROWSER - 'BACK BUTTONS '
# STACKS ARE USED TO EASILY REVERSE A WORD WITHOUT USING INDEX

# # QUESTION : Empty sequence  is given .. then do the following :
# # A. Push the element x into the stack
# # B. Delete the topmost element  in stack
# # C. Display  the biggest number in the stack
#
# N = int(input())
# stack = []
#
# for i in range(N):
#     line = input()
#     query = line[0]
#
#     if query == '1':
#         val = int(line[2:1])
#         if len(stack) == 0:
#             stack.append(val)
#         else:
#             currentMax = stack[-1]
#             stack.append(val if val > currentMax else currentMax)
#     elif query == '2':
#         stack.pop()
#     else:
#         print(stack[-1])

print("-------QUEUES--------")


class QUEUE:
    def __init__(self):
        self.queue = []

    def enQueue(self, item):
        self.queue.append(item)

    def deQueue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)


# MAKING  AN OBJECT 'Q' OF CLASS ---> QUEUE
Q = QUEUE()
# enQ ---> ADDING AN ELEMENT  AT THE END OF THE Q
print("ADDING 100 as a VALUE IN THE QUEUE ")
Q.enQueue(10)
Q.enQueue(100)
# deQ ---> REMOVING AN ITEM FROM THE END OF THE Q
Q.deQueue()

# FUNCTION FOR DISPLAYING THE Q
Q.display()

# Time complexity : O(1) ---> Constant Time
# Used in OS, Web Server,Games

print("-------LINKED LISTS--------")


# Time Complexity :
# Searching : O(n) ---> Need to go over every element

class Node:
    def __int__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkList:
    def __init__(self):
        self.head = None
        