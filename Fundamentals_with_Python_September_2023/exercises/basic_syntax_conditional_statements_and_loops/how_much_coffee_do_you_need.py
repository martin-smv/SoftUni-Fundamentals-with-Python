command = input()
sum_of_coffees = 0

while command != "END":
    if command == "coding"\
            or command == "dog"\
            or command == "cat"\
            or command == "movie":
        sum_of_coffees += 1
    elif command == "CODING"\
            or command == "DOG"\
            or command == "CAT"\
            or command == "MOVIE":
        sum_of_coffees += 2
    command = input()

if sum_of_coffees > 5:
    print("You need extra sleep")
else:
    print(sum_of_coffees)