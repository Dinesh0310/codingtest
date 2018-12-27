'''Write a function that accepts a list and doubles each value in the list. When no input parameter is provided, return an empty list.'''
def check_list_len(a):
    b = []
    for i in a:
        b.append(i*2)
    return b

lst = list(map(int,input().split()))
if len(lst):
    print(check_list_len(lst))
else:
    a = list()
    print(a)