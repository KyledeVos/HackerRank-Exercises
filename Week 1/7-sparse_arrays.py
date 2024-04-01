

def matchingStrings(strings, queries):
    string_dict = {}

    for string in strings:
        string_dict[string] = string_dict.get(string, 0) + 1
    counts = []
    for q_string in queries:
        counts.append(string_dict.get(q_string, 0))

    return counts
    

if __name__ == '__main__':

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    print(res)
