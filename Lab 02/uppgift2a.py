

def frame(s):
	print("*"*(len(s)+4))
	print("*",s,"*")
	print("*"*(len(s)+4))

def triangle(rows):
	for i in range(rows):
		print("*"*(2*i+1))

def flag(n):
	for i in range(n*4):
		print(("*"*n*10) + (2*n*(" ")) + ("*"*n*10))
	for i in range(n):
		print("")
	for i in range(n*4):
		print(("*"*n*10) + (2*n*(" ")) + ("*"*n*10))


frame('Välkommen till Python')
print("\n")
triangle(3)
print("\n")
flag(1) 