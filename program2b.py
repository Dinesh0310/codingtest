'''  Write a function to test if a list contains any items. Return 'EMPTY' if it does not contain any items and 'NOT EMPTY' if it does ''' 

a = [1]

def listval(a):
  if a:
    print('NOT EMPTY')
  else:
    print('EMPTY')
listval(a)