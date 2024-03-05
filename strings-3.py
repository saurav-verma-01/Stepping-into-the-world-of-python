age = 25

print("My age is " + str(age) + " years.")
print("My age is {0} years.".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}.".format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

# String Formatting

for i in range(1,13):
  print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i**2, i**3))

print()
print()

for i in range(1,13):
  print("No. {0:<2} squared is {1:<3} and cubed is {2:<4}".format(i, i**2, i**3))

print()

print("Pi is approximately {0:12}".format(22/7))