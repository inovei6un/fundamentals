rooms = int(input())
overall_chairs = 0
overall_visitors = 0
free_chairs = 0
needed_chairs = 0

for room in range(1, rooms + 1):
    current_room = room
    chairs_and_visitors = (input().split(' '))
    chairs = len(chairs_and_visitors[0])
    visitors = int(chairs_and_visitors[1])
    overall_chairs += chairs
    overall_visitors += visitors
    if chairs > visitors:
        free_chairs += chairs - visitors
    elif visitors > chairs:
        needed_chairs = visitors - chairs
        print(f"{needed_chairs} more chairs needed in room {current_room}")
if overall_chairs >= overall_visitors:
    print(f"Game On, {free_chairs} free chairs left")
