from collections import deque

henry_money = [int(el) for el in input().split()]        #LIFO
prices = deque([int(el) for el in input().split()])      #FIFO
food_count = 0

while henry_money and prices:
    current_money = henry_money.pop()
    current_price = prices.popleft()

    if current_money == current_price:
        food_count += 1
        continue
    elif current_money > current_price:
        food_count += 1
        current_money -= current_price
        if len(henry_money) > 1:
            henry_money[-1] += current_money
        else:
            break
    else:
        continue

if food_count >= 4:
    print(f"Gluttony of the day! Henry ate {food_count} foods.")
elif 0 < food_count < 4:
    if food_count == 1:
        print(f"Henry ate: {food_count} food.")
    else:
        print(f"Henry ate: {food_count} foods.")
else:
    print(f"Henry remained hungry. He will try next weekend again.")