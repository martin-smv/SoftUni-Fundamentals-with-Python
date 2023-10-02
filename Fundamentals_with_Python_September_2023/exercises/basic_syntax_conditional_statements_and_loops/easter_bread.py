current_budget = float(input())
one_kilo_flour_price = float(input())
pack_of_eggs_price = one_kilo_flour_price * 0.75
one_liter_of_milk_price = one_kilo_flour_price * 0.25 + one_kilo_flour_price


eggs_counter = 0
loaves_counter = 0
while current_budget > 0:
    current_budget -= one_kilo_flour_price + pack_of_eggs_price + (one_liter_of_milk_price / 4)
    if current_budget < 0:
        current_budget += one_kilo_flour_price + pack_of_eggs_price + (one_liter_of_milk_price / 4)
        break
    loaves_counter += 1
    eggs_counter += 3
    if loaves_counter % 3 == 0:
        egg_loss = loaves_counter - 2
        eggs_counter -= egg_loss

print(f"You made {loaves_counter} loaves of Easter bread! "
      f"Now you have {eggs_counter} eggs and {current_budget:.2f}BGN left.")