def plant_garden(garden_space, *args, **kwargs):

    allowed_flowers = {plant: space for plant, space in args}
    sorted_planting_requests = sorted(kwargs.items())
    planted = {}

    for plant, pieces in sorted_planting_requests:
        if plant not in allowed_flowers:
            continue
        each_flower_space = allowed_flowers[plant]
        possible_pieces = int(garden_space / each_flower_space)
        plants_to_plant = min(possible_pieces, pieces)

        if plants_to_plant > 0:
            planted[plant] = plants_to_plant
            garden_space -= plants_to_plant * each_flower_space
        if garden_space <= 0.0:
            break

    result = ["Planted plants:"]
    [result.append(f"{plant}: {planted[plant]}") for plant in sorted(planted)]
    formated_planted_pcs = "\n".join(result)

    if all(planted.get(pt, 0) == qty for pt, qty in kwargs.items() if pt in allowed_flowers):
        return f"All plants were planted! Available garden space: {garden_space:.1f} sq meters.\n{formated_planted_pcs}"
    return f"Not enough space to plant all requested plants!\n{formated_planted_pcs}"



print(plant_garden(50.0,("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0),rose=10, tulip=20))
print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))