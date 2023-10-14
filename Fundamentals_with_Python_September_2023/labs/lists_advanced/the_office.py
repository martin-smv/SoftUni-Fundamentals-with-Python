def improve_happiness():
    improved_happiness = [happiness * improvement_factor for happiness in employees_happiness]

    return improved_happiness


employees_happiness = list(map(int, input().split()))
improvement_factor = int(input())

average_happiness = sum(improve_happiness()) / len(improve_happiness())
happy_count = len([happiness for happiness in improve_happiness() if happiness >= average_happiness])

if happy_count >= len(improve_happiness()) / 2:
    print(f"Score: {happy_count}/{len(improve_happiness())}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{len(improve_happiness())}. Employees are not happy!")