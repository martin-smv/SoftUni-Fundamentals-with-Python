from math import ceil

budget = float(input())
students = int(input())
package_of_flour_price = float(input())
single_egg_price = float(input())
single_apron_price = float(input())

free_packages = 0
for number_of_student in range(1, students + 1):
    if number_of_student % 5 == 0:
        free_packages += 1

flour_cost = students * package_of_flour_price - free_packages * package_of_flour_price

eggs_cost = (10 * single_egg_price) * students

apron_cost = ceil(students + students * 0.20) * single_apron_price

total_cost = flour_cost + eggs_cost + apron_cost

if budget >= total_cost:
    print(f"Items purchased for {total_cost:.2f}$.")
else:
    needed_money = total_cost - budget
    print(f"{needed_money:.2f}$ more needed.")