
def make_list(number):
    names = []
    for item in range(number):
        names.append(input("type name "))
    return names

number = int(input("hoeveel "))
names = make_list(number)

# for x in number:
#     print(x)

for x in names:
    print(x)
    if x[0] == "A":
        print(names)

