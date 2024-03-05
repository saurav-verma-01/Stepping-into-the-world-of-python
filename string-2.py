parrot = "Norwegian Blue"

print(parrot[0:6:2])
print(parrot[0::3])

number = "9,254;785:963 458,749;632"

separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()

print([int(val) for val in values])
# print(parrot[::-1])


# print(parrot)
# print(parrot[3])
# print(parrot[-1])
# print()
# print(parrot[-11])
# print(parrot[-8])
# print(parrot[-6])

# print(parrot[:])