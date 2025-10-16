from collections import deque

worms = [int(el) for el in input().split()]                 #LIFO
holes =  deque([int(el) for el in input().split()])         #FIFO
matches = 0
worms_size = len(worms)

while worms and holes:
    current_worm = worms.pop()
    current_hole = holes.popleft()
    if current_worm == current_hole:
        matches += 1
        continue
    else:
        current_worm -= 3
        if current_worm > 0:
            worms.append(current_worm)

print(f"Matches: {matches}" if matches != 0 else "There are no matches.")

if matches != worms_size:
    print(f"Worms left: {', '.join(map(str, worms))}" if worms else "Worms left: none")
else:
    print("Every worm found a suitable hole!")

print(f"Holes left: {', '.join(map(str, holes))}" if holes else "Holes left: none")


