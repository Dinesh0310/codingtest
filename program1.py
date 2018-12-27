''' Write a function that accepts two arbitrary strings and returns a new string containing only the unique characters present in both inputs'''
str1 = str(input('enter str1'))
str2 = str(input('enter str2'))
def unichar(a,b):
  uni = ''
  for i in range(len(a)):
    for j in range(len(b)):
      if a[i]==b[j] and a[i] not in uni:
        uni = uni+a[i]
  return uni
print(unichar(str1,str2))