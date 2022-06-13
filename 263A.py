for _ in range(5):
    str = input()
    if '1' in str:
        print(abs(_ - 2) + abs(str.index('1') // 2 - 2))