original_deck = input().split()
count_of_shuffles = int(input())
for shuffle in range(count_of_shuffles):
    half_of_the_deck = len(original_deck) // 2
    left_half = original_deck[0:half_of_the_deck]
    right_half = original_deck[half_of_the_deck:]
    shuffled_deck = []
    for current_card in range(len(left_half)):
        shuffled_deck.append(left_half[current_card])
        shuffled_deck.append(right_half[current_card])
    original_deck = shuffled_deck
print(shuffled_deck)