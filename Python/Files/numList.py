
charstr = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM"
chars = list(charstr)
nums = [str(i) for i in range(1,39)]
with open("data.txt" , "r") as f:
	data = f.read()
output = ""

for i in range(len(data)):
	if data[i] in chars:
		pos = chars.index(data[i])
		output = output + nums[pos] + " "
	elif data[i] == " ":
		output = output + "\t"
	else:
		output = output + data[i] + " "


	
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]


# table = dict(zip(letters,numbers))


print("Output of the two lists " + output)

