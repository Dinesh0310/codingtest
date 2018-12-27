'''  Write a function that accepts an integer and returns True if the input is between 4 and 10, inclusive; otherwise, return False''' 

a=int(input('enter an integer'))

def numval(num):
  
	if num in range(4,11):
    
		print('TRUE')
  
	else:
    
		print('FALSE')

numval(a)