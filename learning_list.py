python_list = [1,1,2,3,4,4,5,5,6,7,8,9,9,10]

unique_list = list(set(python_list))

seen = set()
i = 0

while i < len(python_list):
    if python_list[i] in seen:
        python_list.pop(i)
    else:
        seen.add(python_list[i])
        i += 1

print(python_list)

