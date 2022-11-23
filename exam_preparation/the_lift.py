people = int(input())
state_of_lift_str = [i for i in input().split(' ')]
state_of_lift = list(map(int, state_of_lift_str))

for wagon in range(len(state_of_lift)):
    while state_of_lift[wagon] < 4:
        if people == 0:
            break
        people -= 1
        state_of_lift[wagon] = state_of_lift[wagon] + 1
for wagon in state_of_lift:
    if wagon < 4:
        print(f"The lift has empty spots!")
        break
if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
state_of_lift = list(map(str, state_of_lift))
output_string = ' '.join(state_of_lift)
print(output_string)
