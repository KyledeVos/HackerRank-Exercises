def marsExploration(s):
    # Write your code here

    deviation_count = 0

    for count, char in enumerate(s):
        if (count+1)%3 == 2:
            if char != "O":
                deviation_count += 1

        elif char != "S":
            deviation_count += 1

    return deviation_count


if __name__ == '__main__':

    s = input()

    result = marsExploration(s)

    print(result)
