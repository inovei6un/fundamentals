version = list(map(int, (i for i in input().split("."))))
if version[2] < 9:
    version[2] += 1
elif version[2] >= 9:
    version[2] = 0
    if version[1] < 9:
        version[1] += 1
    elif version[1] >= 9:
        version[1] = 0
        version[0] += 1
version = list(map(str, version))
output_string = '.'.join(version)
print(output_string)
