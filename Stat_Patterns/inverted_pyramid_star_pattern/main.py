num = 5

for i in range(num, 0, -1):
    spaces = num - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)
