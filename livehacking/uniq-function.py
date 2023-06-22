def uniq(i):
    have = set()
    o = []
    for elem in i:
        if elem not in have:
            o.append(elem)
            have.add(elem)
    return o

input_list = [2, 3, 1, 10, 3, 3, 1, 10, 5, 2]
output_list = uniq(input_list)

for element in output_list:
    print(element)
