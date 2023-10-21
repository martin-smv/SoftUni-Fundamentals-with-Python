grams_of_food = float(input()) * 1000
grams_of_hay = float(input()) * 1000
grams_of_cover = float(input()) * 1000
guinea_weight = float(input()) * 1000

everything_is_enough = True
for day in range(1, 30 + 1):

    grams_of_food -= 300

    if day % 2 == 0:
        grams_of_hay -= grams_of_food * 0.05

    if day % 3 == 0:
        grams_of_cover -= guinea_weight * (1 / 3)

    if grams_of_food <= 0 or grams_of_hay <= 0 or grams_of_cover <= 0:
        everything_is_enough = False
        break


if everything_is_enough:
    kilogram_food = grams_of_food / 1000
    kilogram_hay = grams_of_hay / 1000
    kilogram_cover = grams_of_cover / 1000
    print(f"Everything is fine! Puppy is happy! Food: {kilogram_food:.2f}, "
          f"Hay: {kilogram_hay:.2f}, "
          f"Cover: {kilogram_cover:.2f}.")
else:
    print("Merry must go to the pet store!")