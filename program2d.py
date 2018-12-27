'''Write a function that accepts a list and doubles each value in the list. When no input parameter is provided, return an empty list.'''
def doublelist(a):
  for i in range(len(a)):
    a[i]=2*int(a[i])
  print(a)
n=input('enter no of list elements')
if n:
  n=int(n)
elif n == '':
  n=0
a=[]
if n:
  for i in range(n):
    g=int(input('inter integer list element'))
    a.append(g)
doublelist(a)