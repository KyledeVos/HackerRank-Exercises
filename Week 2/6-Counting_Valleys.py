
#

def countingValleys(steps, path):
    # Write your code here

    valleys = 0
    in_valley = False
    height = 0

    for step in path:
        if step == "U":
            height += 1
        else:
            height -= 1

        if in_valley is False and height <0:
            in_valley = True
        elif in_valley is True and height >=0:
            valleys += 1
            in_valley = False

    return valleys

if __name__ == '__main__':

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(result)