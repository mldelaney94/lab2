import random
import copy

"""
This function returns a new list that is created by shuffling the elements of the
provided list
:param li: The list to be shuffled
:return shuffled_list: The shuffled list
"""

user_list = input("Put a few comma separated characters\n").split(',')

def shuffle(li):
    i=0
    while i < len(li)*2:
        x = random.randint(0, len(li)-1)
        y = random.randint(0, len(li)-1)
        li[x], li[y] = li[y], li[x]
        i+=1
    return li

print(shuffle(user_list))
