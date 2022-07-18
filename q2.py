'''
    "More Positives than Negatives"

    Write a function called more_positives that takes in a list
    of numbers and returns True if there are more positive numbers 
    than negative numbers in the list, otherwise False.

    Examples:
        more_positives([4, -3, 5]) --> True
        more_positives([4, -6, -2]) --> False
        more_positives([2, -5, 0, 4, -7, 0]) --> False
'''

#Write your function under here
def more_positives([2, -5, 0, 4, -7, 0]):
    p = 0
    n = 0
    for num in more_positives:
        if num >=0:
            p += 1
        if num <0:
            n += 1
        if p > n:
            print(True)
        if n > p:
            print(False)
print(more_positives(2, -5, 0, 4, -7, 0))
        