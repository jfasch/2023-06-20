def uniq(i):
    have = set()
    for elem in i:
        if elem not in have:
            yield elem
            have.add(elem)

input_list = [2, 3, 1, 10, 3, 3, 1, 10, 5, 2]
output = uniq(input_list)

for element in output:
    print(element)
