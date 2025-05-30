number = int(input("Enter the size of the pattern: "))
i = 0

while i <= number:
    for x in range(number):
        print("*", end="")
    print()
    i = i + 1