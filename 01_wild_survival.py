from collections import deque

bee_groups = deque([int(el) for el in input().split()])   #FIFO
bee_eaters = [int(el) for el in input().split()]  #LIFO


while bee_groups and bee_eaters:
    current_bee_eaters = bee_eaters.pop()
    current_bee_group = bee_groups.popleft()
    while current_bee_group > 0 and current_bee_eaters > 0:
        if current_bee_eaters * 7 <= current_bee_group:
            current_bee_group -= current_bee_eaters * 7
            current_bee_eaters = 0
        else:
            current_bee_eaters -= (current_bee_group // 7)
            current_bee_group = 0

    if current_bee_group > 0 and current_bee_eaters == 0:
        bee_groups.append(current_bee_group)
    elif current_bee_group == 0 and current_bee_eaters > 0:
        bee_eaters.append(current_bee_eaters)

print("The final battle is over!")
if not bee_groups and not bee_eaters:
    print("But no one made it out alive!")
elif bee_groups:
    print(f"Bee groups left: {', '.join(map(str, bee_groups))}")
elif bee_eaters:
    print(f"Bee-eater groups left: {', '.join(map(str, bee_eaters))}")
