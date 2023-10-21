def is_full():
    full = False
    for i in state_of_the_lift:
        if i == 4:
            full = True
            break

    return full


people_waiting = int(input())
state_of_the_lift = input().split()

for index in range(len(state_of_the_lift)):
    cabin = int(state_of_the_lift[index])
    free_places = 4 - cabin

    if people_waiting - free_places >= 0:
        people_waiting -= free_places
        cabin += free_places
        state_of_the_lift[index] = str(cabin)
    else:
        cabin += people_waiting
        people_waiting -= free_places
        state_of_the_lift[index] = str(cabin)
        break

if people_waiting < 0 and not is_full():
    print("The lift has empty spots!")
elif people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
print(" ".join(state_of_the_lift))