# finding item in a list
# example

name = ["Shuvam", "Riju", "India", "Coding", "Riju"]

if "Riju" in name:
    position = name.index("Riju")
    count = name.count("Riju")
    print("Item exists in index {}".format(position))
    print("No of items are {}".format(count))
else:
    print("Not Exists")




