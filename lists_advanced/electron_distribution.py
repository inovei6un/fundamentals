electrons = int(input())
filled_shells = list()
n = 0
max_num_in_shell = 0

for position_of_shell in range(1, electrons + 1):
    n += 1
    max_num_in_shell = 2 * position_of_shell ** 2
    electrons -= max_num_in_shell
    if electrons > 0:
        filled_shells.append(max_num_in_shell)
    elif electrons == 0:
        filled_shells.append(max_num_in_shell)
    elif electrons < 0:
        if max_num_in_shell - abs(electrons) != 0:
            filled_shells.append(max_num_in_shell - abs(electrons))
        break

print(filled_shells)
