def drive_func(car, distance, fuel, stored_cars):
    if stored_cars[car][1] < fuel:
        print("Not enough fuel to make that ride")
    else:
        stored_cars[car][0] += distance
        stored_cars[car][1] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

    if stored_cars[car][0] >= 100000:
        del stored_cars[car]
        print(f"Time to sell the {car}!")

    return stored_cars


def refuel_func(car, fuel, stored_cars):
    refueled_fuel = 0
    if stored_cars[car][1] + fuel <= 75:
        refueled_fuel = (stored_cars[car][1] + fuel) - stored_cars[car][1]
        stored_cars[car][1] += fuel
    else:
        refueled_fuel = 75 - stored_cars[car][1]
        stored_cars[car][1] = 75

    print(f"{car} refueled with {refueled_fuel} liters")

    return stored_cars


def revert_func(car, kilometers, stored_cars):
    if stored_cars[car][0] - kilometers >= 10000:
        stored_cars[car][0] -= kilometers
        print(f"{car} mileage decreased by {kilometers} kilometers")
    else:
        stored_cars[car][0] = 10000

    return stored_cars


stored_cars = {}

number_of_cars = int(input())

for i in range(number_of_cars):
    current_car = input().split("|")
    car = current_car[0]
    mileage = int(current_car[1])
    fuel = int(current_car[2])
    stored_cars[car] = [mileage, fuel]

command = input()
while command != "Stop":
    command = command.split(" : ")

    if command[0] == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        stored_cars = drive_func(car, distance, fuel, stored_cars)

    elif command[0] == "Refuel":
        car = command[1]
        fuel = int(command[2])
        stored_cars = refuel_func(car, fuel, stored_cars)

    elif command[0] == "Revert":
        car = command[1]
        kilometers = int(command[2])
        stored_cars = revert_func(car, kilometers, stored_cars)

    command = input()

for car, value in stored_cars.items():
    mileage = value[0]
    fuel = value[1]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")