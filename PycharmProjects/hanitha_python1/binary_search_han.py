"""
Docstring: This module contains Binary search implementation
"""
l = [6, 2, 3, 4, 5]
key = 2
l.sort()


def search(l, key):
    """ Linear search:Searches a key value in a given list using simple for loop.Returns True if key value found."""
    for i in l:
        if key == i:
            return True
    return False


print(search(l, key))


def bin_search(l, key):
    """ Binary search: Input a list and key to be searched. Returns True if key found."""
    mid = len(l) // 2
    if key == l[mid]:
        return True
    elif key < l[mid]:
        if key in l[:mid]:
            return True
    elif key > l[mid]:
        if key in l[(mid + 1):]:
            return True
    return False


# print(bin_search(l,key))

def bi_search(l, key):
    """ Binary search: Input a list and key to be searched. Returns True if key found.This uses recursive method"""
    if len(l) == 0:
        return False
    else:
        mid = len(l) // 2
        if key == l[mid]:
            return True
        elif key < l[mid]:
            return bi_search(l[:mid], key)
        elif key > l[mid]:
            return bi_search(l[(mid + 1):], key)

# print(bi_search(l,key))
