'''
    "Duplicate W's in a String"

    Write a function called duplicate_w that takes in a string
    and duplicates w's in that string.

    Examples:
        duplicate_w("wow") --> "wwoww"
        duplicate_w("www.google.com") --> "wwwwww.google.com"
        duplicate_w("apple") --> "apple"
'''

#Write your function under here
def duplicate_w(str):
    dup_w = ""
    for i in range(len(str)):
        if str[i] == w:
            if str[i] != w:
                dup_w = dup_w + str[i] + "w"
                dup_w = dup_w + str[i]
    print(dup_w)
    print(duplicate_w(str))
               
        