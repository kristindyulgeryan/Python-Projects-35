import random

print("🧑🏼‍🍳 RANDOM RECIPE GENERATOR🧑🏼‍🍳")

proteins = ["chicken", "beef", "tofu", "fish", "eggs"]
veggies = ["brocoli", "carrots", "spinach", "bell peppers", "mushrooms"]
carbs = ["rice", "pasta", "potatoes", "quinoa", "bread"]
methods = ["baked", "grilled", "stir-fried", "roasted", "sauteed"]
flavors = ["garlic", "lemon", "spicy", "herb", "sweet & sour"]


while True:
    protein = random.choice(proteins)
    veggie = random.choice(veggies)
    carb = random.choice(carbs)
    method = random.choice(methods)
    flavor = random.choice(flavors)

    print(
        f"\nYour random recipe: {flavor} {method} {protein} with {veggie} and {carb}")

    if not input("\nGenerate another one? (y/n): ").lower().startswith("y"):
        print("Goodbye!")
        break

