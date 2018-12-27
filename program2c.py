'''Write a function that accepts a file name and a string and writes the string to the file with the given file name'''

filename = str(input('enter file name'))

string = str(input('enter string name'))

with open(filename,'w') as f:
  
	f.write(string)