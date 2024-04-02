def lonelyinteger(a):

    num_dict = {}
    for val in a:
        num_dict[val] = num_dict.get(val, 0) + 1

    for key, val in num_dict.items():
        if val == 1:
            return key


if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    print(result)

