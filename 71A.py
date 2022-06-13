for _ in range(int(input())):
    str = input()
    if len(str) > 10:
        print(str[0], len(str) - 2, str[-1], sep='')
    else:
        print(str)