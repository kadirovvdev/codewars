#36

def sort_cards(cards):
    return sorted(cards, key="A23456789TJQK".index)

#37

def sort_grades(lst):
    empty_list = []

    for element in lst:
        lst.sort(key=get_value)

    return lst


def get_value(wht):
    value = {

        'VB': -2,
        'V0': -1,
        'V0+': 0,
        'V1': 1,
        'V2': 2,
        'V3': 3,
        'V4': 4,
        'V5': 5,
        'V6': 6,
        'V7': 7,
        'V8': 8,
        'V9': 9,
        'V10': 10,
        'V11': 11,
        'V12': 12,
        'V13': 13,
        'V14': 14,
        'V15': 15,
        'V16': 16,
        'V17': 17

    }

    return value[wht]


#38

def queue(_arr, pos):
    out = 0
    for i in range(len(_arr)):
        if i <= pos:
            out += min(_arr[i], _arr[pos])
        else:
            out += min(_arr[pos] - 1, _arr[i])

    return out


#39


from operator import itemgetter

def sort_it(list_, n):
    return ', '.join(sorted(list_.split(', '), key=itemgetter(n - 1)))


#40

def sort_dict(d):
	a = []
	for x in d:
		a.append((x, d[x]))

	for i in range(0, len(a)):
		for j in range(i + 1, len(a)):
			if a[i][1] < a[j][1]:
				temp = a[j]
				a[j] = a[i]
				a[i] = temp

	return a


#41


def closest(l):
    a = list(map(abs,list(set(l))))
    if a.count(min(a))>1:
        return None
    a = min(a)
    return a if a in list(set(l)) else -a


#42

def plastic_balance(a):
    return plastic_balance(a[1:-1]) if a and a[0]+a[-1] != sum(a[1:-1]) else a

#43

def unite_unique(*arg):
    res = []
    for arr in arg:
        for val in arr:
            if not val in res: res.append(val)
    return res

#44

def elements_sum(arr, d=0):
    a=len(arr)
    res=0
    for i in arr:
        if len(i)>=a:
            res+=i[a-1]
        else:
            res+=d
        a-=1
    return res

#45

def compress(_s):
    s = _s.lower().split()
    arr = []
    for i in s:
        if i not in arr:
            arr.append(i)
    return ''.join([str(arr.index(i)) for i in s])


#46

def sort_it(un):
    for g in range(len(un)):
        for h in range(len(un)-1):
            cmp1=un[h]
            cmp2=un[h+1]
            if type(un[h])==list:
                cmp1=un[h][0]
            if type(un[h+1])==list:
                cmp2=un[h+1][0]
            if cmp1>cmp2:
                un[h],un[h+1]=un[h+1],un[h]
    return un