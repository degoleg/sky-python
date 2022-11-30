filename = "data.txt"
f = open(filename, "r")
items = {}
for line in f:
    item_data = line.strip().split()
    title = item_data[0]
    value = item_data[1]
    items[title] = value
print(items)
f.close()
