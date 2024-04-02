

def flippingBits(n):

    def invert_num(val):
        if val == 1:
            return 0
        else:
            return 1
        
    sum = 0
    count = 0
    
    # Convert to binary and invert at the same time
    while n>=2:
        
        if invert_num(n%2) == 1:
            sum += 2**count
        n = int(n/2)
        count += 1
    
    if n == 1:
        count += 1


    for i in reversed(range(count, 32)):
        sum += 2**i

    return sum

if __name__ == '__main__':


    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        print(result)
