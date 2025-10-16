def cookbook(*args):
    recipe_categories = {}

    for name, cuisine, ingredients in args:
        if cuisine not in recipe_categories:
            recipe_categories[cuisine] = []
        recipe_categories[cuisine].append((name, ingredients))

    sorted_recipes_categories = sorted(recipe_categories.items(),
                                       key=lambda r: (-len(r[1]), r[0]))
    result = ''
    for cuisine, recipes in sorted_recipes_categories:
        sorted_recipes = sorted(recipes, key=lambda x: x[0])
        result += f"{cuisine} cuisine contains {len(sorted_recipes)} recipes:\n"
        for name, ingredients in sorted_recipes:
            result += f"  * {name} -> Ingredients: {', '.join(ingredients)}\n"
    return result.strip()

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
