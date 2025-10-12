from collections import deque

strength = [int(el) for el in input().split()]  #LIFO-stack
accuracy = deque([int(el) for el in input().split()])   #FIFO-deque
goals = 0

while strength and accuracy:
    current_strength = strength[-1]
    current_accuracy = accuracy[0]
    total_sum = current_strength + current_accuracy

    if total_sum == 100:
        strength.pop()
        accuracy.popleft()
        goals += 1
    elif total_sum < 100:
        if current_strength < current_accuracy:
            strength.pop()
        elif current_strength > current_accuracy:
            accuracy.popleft()
        else:
            current_strength = current_strength + current_accuracy
            strength[-1] = current_strength
            accuracy.popleft()
    else:
        current_strength -= 10
        strength[-1] = current_strength
        accuracy.append(current_accuracy)
        accuracy.popleft()

if goals == 3:
    print("Paul scored a hat-trick!")
elif goals == 0:
    print("Paul failed to score a single goal.")
elif goals > 3:
    print("Paul performed remarkably well!")
elif 0 < goals < 3:
    print("Paul failed to make a hat-trick.")

if goals > 0:
    print(f"Goals scored: {goals}")

if strength:
    print(f"Strength values left: {', '.join([str(el) for el in strength])}")
if accuracy:
    print(f"Accuracy values left: {', '.join([str(el) for el in accuracy])}")















