from collections import deque

substance_quantities = [int(el) for el in input().split(', ')]           #LIFO
crystal_energy = deque([int(el) for el in input().split(', ')])          #FIFO

#input 40, 5, 80, 60, 75, 60, 65, 70
#input 20, 35, 45, 25, 10, 30, 15

crafted_potions = {
    "Brew of Immortality":	110,
    "Essence of Resilience": 100,
    "Draught of Wisdom": 90,
    "Potion of Agility": 80,
    "Elixir of Strength": 70,
}
created_potions = []

while substance_quantities and crystal_energy:
    current_substance = substance_quantities.pop()
    current_energy = crystal_energy.popleft()
    total_energy = current_substance + current_energy

    for potion_name, needed_energy in crafted_potions.items():
        if potion_name not in created_potions:
            if total_energy == needed_energy:
                created_potions.append(potion_name)
                continue  #това може би е на друго място

            elif total_energy > needed_energy:
                current_energy -= 20
                if current_energy > 0:
                    crystal_energy.append(current_energy)
            else:
                current_energy -= 5
                if current_energy > 0:
                    crystal_energy.append(current_energy)

if len(created_potions) == 5:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")
if created_potions:
    print(f"Crafted potions: {', '.join([str(el) for el in created_potions])}")
if substance_quantities:
    sorted_substances = sorted(substance_quantities, reverse=True)
    print(f"Substances: {', '.join([str(el) for el in sorted_substances])}")
if crystal_energy:
    print(f"Crystals: {', '.join([str(el) for el in crystal_energy])}")

















