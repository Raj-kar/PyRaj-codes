'''
A
B B
C C C 
D D D D
E E E E E
'''
start = "C"
end = "H"

for i in range(ord(start), ord(end)+1):
	for j in range(ord(start), i+1):
		print(chr(i), end = ' ')
	print()