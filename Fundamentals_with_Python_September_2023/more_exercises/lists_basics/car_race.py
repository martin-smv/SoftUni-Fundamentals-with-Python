numbers = input().split()
middle_index = len(numbers) // 2
left_racer = numbers[:middle_index]
right_racer = numbers[:middle_index:-1]
left_racer_total_time = 0
right_racer_total_time = 0

for time in left_racer:
    time = int(time)
    if time == 0:
        left_racer_total_time -= left_racer_total_time * 0.20
    left_racer_total_time += time
for time in right_racer:
    time = int(time)
    if time == 0:
        right_racer_total_time -= right_racer_total_time * 0.20
    right_racer_total_time += time

if left_racer_total_time < right_racer_total_time:
    print(f"The winner is left with total time: {left_racer_total_time:.1f}")
else:
    print(f"The winner is right with total time: {right_racer_total_time:.1f}")