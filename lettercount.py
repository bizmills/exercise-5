f = open("twain.txt")
filetext = f.read()

for char in filetext:
	print char

ascii_count = [ord(c) for c in filetext] # converts text to ascii numbers
	print ascii_count

#ascii_count.count(filetext)


f. close()