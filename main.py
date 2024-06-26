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


#12

def partlist(arr):
    new_arr = []
    for x in range(1,len(arr)):
        y = ' '.join(arr[:x])
        z = ' '.join(arr[x:])
        new_arr.append((y,z))
    return new_arr



#13

def or_arrays(arr1, arr2, n=0):
    result = []

    for i in range(max(len(arr1), len(arr2))):

        a = b = n;

        if i < len(arr1):
            a = arr1[i]

        if i < len(arr2):
            b = arr2[i]

        result.append(b | a);

    return result



#14


def remove_smallest(numbers):
    if len(numbers) < 1:
        return numbers
    idx = numbers.index(min(numbers))
    return numbers[0:idx] + numbers[idx+1:]


#15

bin_to_colors = {1: "black", 2: "brown", 3:"dark brown", 4: "white", 5: "grey", 6: "light brown"}
colors_to_bin = {v: k for k, v in bin_to_colors.items()}

def bear_fur(bears):
    return bin_to_colors.get(sum(colors_to_bin.get(k, 7) for k in set(bears)), "unknown")


#16


def sum_it_up(a):
    return sum(int(n, b) for n, b in a)

#17
from collections import defaultdict

def stem_and_leaf(a):
    d = defaultdict(list)
    for x in a:
        d[x//10].append(x % 10)
    return {x: sorted(y) for x, y in d.items()}


#18
def replace_all(obj, find, replace):
    for i, o in enumerate(obj):
        if o == find:
            try:
                obj[i] = replace
            except:
                obj = obj.replace(obj[i], replace, 1)
    return obj


#19

def reverse_invert(lst):
    r = []
    for i in lst:
        if isinstance(i,int):
            if i < 0:
                i = int(str(i)[1:][::-1])
            else:
                i = -int(str(i)[::-1])
            r.append(i)
    return r

#20

def candies(s):
    if not s or len(s) == 1:
        return -1
    return len(s) * max(s) - sum(s)

#21
def get_new_notes(salary, bills):
    return max((salary - sum(bills)), 0) // 5



#22

def min_max(lst):
  return [min(lst), max(lst)]

#23


def all_rationals():
    yield (1, 1)
    for a, b in all_rationals():
        yield from [(a, a + b), (a + b, b)]


#24

def row_sum_odd_numbers(n):
    return n ** 3

#25

def is_monotone(heights):
    return sorted(heights) == heights


#26

def duplicate_sandwich(arr):
    pos = {}
    for i, x in enumerate(arr):
        if x in pos:
            return arr[pos[x] + 1 : i]
        pos[x] = i

























#26
def duplicate_sandwich(arr):
    pos = {}
    for i, x in enumerate(arr):
        if x in pos:
            return arr[pos[x] + 1 : i]
        pos[x] = i


