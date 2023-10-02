year = int(input())
special_year = False
while not special_year:
    year += 1
    year_as_a_string = str(year)
    if len(year_as_a_string) == len(set(year_as_a_string)):
        print(year)
        special_year = True