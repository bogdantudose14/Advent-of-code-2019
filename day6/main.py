
#Adding up the size of the subtrees for part 1

# Dictionary = {}
#
# for line in open('data.txt').readlines():
#     a,b = line.strip().split(')')
#     if a not in Dictionary:
#         Dictionary[a] = []
#     Dictionary[a].append(b)
#
# # print(len(Dictionary))
#
# def function(key):
#     result=0;
#     for value in Dictionary.get(key,[]):
#         result+=1
#         result+=function(value) # recursive call for all the values
#     return result
#
# result=0
#
# for key in Dictionary:
#     result+=function(key)
#
# print(result)


####### part 2 ##########

#Distances in a tree Algorithm - Breadth First Search


from collections import deque

Dictionary = {}

for line in open('data.txt').readlines():
    a,b = line.strip().split(')')
    if a not in Dictionary:
        Dictionary[a] = []
    if b not in Dictionary:
        Dictionary[b] = []
    Dictionary[a].append(b)
    Dictionary[b].append(a)

DistancesDictionary = {}
Queue = deque()

Queue.append(('YOU',0))

while Queue:  # every time you explre the node
    elem,distance = Queue.popleft() # grab it
    if elem in DistancesDictionary:
        continue
    DistancesDictionary[elem] = distance
    for child in Dictionary[elem]: # for all of its children
        Queue.append((child,distance+1)) # if the distance to its parent is d, the distance to the child is d+1
print(DistancesDictionary['SAN']-2) # or starting with 'SAN' and compute the distance to 'YOU'

#substract 2 for not counting the start and finish nodes


# def function(key):
#     result=0;
#     for value in Dictionary.get(key,[]):
#         result+=1
#         result+=function(value) # recursive call for all the values
#     return result
#
# result=0
#
# for key in Dictionary:
#     result+=function(key)

# print(result)


