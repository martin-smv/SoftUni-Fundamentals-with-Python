def distribute(nums, min_wealth):
    for i in range(len(nums)):
        difference = min_wealth - nums[i]
        index_of_max_num = nums.index(max(nums))

        if nums[i] < min_wealth:
            nums[i] += difference

            if max(nums) - difference < min_wealth:
                return "No equal distribution possible"
            nums[index_of_max_num] = max(nums) - difference

    return nums


population = [int(s) for s in input().split(", ")]
minimum_wealth = int(input())

print(distribute(population, minimum_wealth))