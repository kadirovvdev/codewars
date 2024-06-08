#https://www.codewars.com/kata/search/my-languages?q=&r%5B%5D=-7&tags=Lists&beta=false&order_by=sort_date%20desc


#1


def sentence(list_):
    words = {}
    for entry in list_:
        for key, value in entry.items():
            words[int(key)] = value
    return ' '.join(word[1] for word in sorted(words.items()))

#2
def digitize(n):
    return [int(d) for d in str(n)]

#3
def convert_hash_to_array(dct):
    return sorted(list(item) for item in dct.items())
#4
def copy_list(l):
    return list(l)
#5
from itertools import accumulate

def add(lst):
    return list(accumulate(lst))

#6
def double_every_other(lst):
    x = []
    for i in range(len(lst)):
        if i % 2 != 0:
            x.append(lst[i] * 2)
        else:
            x.append(lst[i])
    return x



#7
def filter_list(l):
    new_list =[]
    for x in l:
        if type(x) != str:
            new_list.append(x)
    return new_list

#8

def inverse_slice(items, a, b):
    del items[a:b]
    return items

#9

def find_children(arr1,arr2):
    L=[]
    for i in arr2:
        if i in arr1:
            if i not in L:
                L.append(i)
    L.sort()
    return L

#10

from statistics import mean

def test(r):
    dct = {'l': 0, 'a': 0, 'h': 0}
    for n in r: dct[ 'lah'[(n>6) + (n>8)] ] += 1
    return [round(mean(r), 3), dct] + ['They did well'] * (sum(dct.values()) == dct['h'])

#11

def reverse_middle(lst):
    l = len(lst)//2 - 1
    return lst[l:-l][::-1]



