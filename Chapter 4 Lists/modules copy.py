import copy

spam = ['A', 'B','C','D']
print(id(spam))
print('\n')
cheese = copy.copy(spam)
print(id(cheese))
cheese[1] =42
print(spam)
print(cheese)