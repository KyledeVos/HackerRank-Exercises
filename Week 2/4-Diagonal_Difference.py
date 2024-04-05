

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    left_diag = 0
    right_diag = len(arr)-1

    left_sum = 0
    right_sum = 0

    for sub_array in arr:
        left_sum += sub_array[left_diag]
        right_sum += sub_array[right_diag]
        left_diag += 1
        right_diag -=1

    print(left_sum)
    print(right_sum)

    return abs(left_sum - right_sum)


if __name__ == '__main__':


    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)