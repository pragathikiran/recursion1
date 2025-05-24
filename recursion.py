def build_pyramid(n,current=1):
    if current > n:
        return
    spaces = ' ' * (n - current)
    stars  = '*' * (2 * current - 1)
    print(spaces + stars)
    build_pyramid(n, current + 1)

levels = int(input("enter the number of leavels"))

print("\nhere is your pyramid\n")
build_pyramid(levels)