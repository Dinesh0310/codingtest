'''  Write a function to test if a list contains any items. Return 'EMPTY' if it does not contain any items and 'NOT EMPTY' if it does ''' 
def listval(a):
  if len(a):
    print('NOT EMPTY')
  else:
    print('EMPTY')

lis = list(map(int,input().split()))
print(listval(lis))