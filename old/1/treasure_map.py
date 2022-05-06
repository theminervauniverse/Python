row1 = ["😂", "😂", "😂"]
row2 = ["🤒", "🤒", "🤒"]
row3 = ["😍", "😍", "😍"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = str(input("Where do you want to put the treaure?\n"))
row = int(position[0])
# row_final = map[row - 1]
# print(row_final)
vertical = int(position[1])
# row_final[vertical - 1] = "X"
# print(vertical_final)
# we can also do this like this
map[row - 1][vertical - 1] = "x"
print(f"{row1}\n{row2}\n{row3}")