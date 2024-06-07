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



