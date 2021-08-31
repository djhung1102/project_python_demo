colors = ["red" , "green" , "blue", "yellow"]

colors.append("pink")	#thêm 1 phần tử vào vị trí cuối cùng của list

print(colors)

colors.remove(colors[1])	#xóa đi 1 phần tử ở vị trí số 1
#colors.remove("green")

print(colors)

colors.pop()	#xóa đi phần tử cuối cùng trong list
print(colors)

colors.insert(1, "black")	#thêm phần tử vào vị trí số 1
print(colors)

print(colors.index("red"))	#tìm vị trí phần tử red trong list

#tìm vị trí của green trong list
colors = ["red" , "green" , "blue", "yellow", "green"]
print(colors)
green_index = []
for i in range(len(colors)):
	if colors[i] == "green":
		green_index.append(i)
print(green_index)

#đếm số lần xuất hiện của phần tử green trong list
print(colors.count("green"))
