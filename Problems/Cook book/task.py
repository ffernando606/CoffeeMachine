pasta = "tomato_, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"
ingredient = input()


recipes = [pasta, apple_pie, ratatouille, chocolate_cake, omelette]
index = ['pasta', 'apple_pie', 'ratatouille', 'chocolate_cake', 'omelette']
for i in range(5):
    if ingredient in recipes[i]:
        print(str(index[i]).replace("_", " "), "time!")


