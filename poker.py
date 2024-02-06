
from collections import Counter
def value(card):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return values[card[0]]

def is_same_suit(suits):
    return len(set(suits)) == 1

def is_straight(values):
    return all(values[i + 1] - values[i] == 1 for i in range(4))

def n_of_a_kind(n, count_values):
    return any(count == n for count in count_values.values())

def n_of_a_kind_value(n, count_values):
    return [key for key, count in count_values.items() if count == n][0]

def check_royal_flush(values, suits, count_values):
    return [10] if is_same_suit(suits) and is_straight(values) and max(values) == 14 else None

def check_straight_flush(values, suits, count_values):
    if is_same_suit(suits):
        if is_straight(values):
            return [9, max(values)]
        if values == [2, 3, 4, 5, 14]:
            return [9, 5]
    return None

def check_four_of_a_kind(values, suits, count_values):
    if n_of_a_kind(4, count_values):
        four_of_a_kind_value = n_of_a_kind_value(4, count_values)
        one_occurrence_value = n_of_a_kind_value(1, count_values)
        return [8, four_of_a_kind_value, one_occurrence_value]
    return None

def check_full_house(values, suits, count_values):
    if n_of_a_kind(3, count_values) and n_of_a_kind(2, count_values):
        three_occurrences_value =  n_of_a_kind_value(3, count_values)
        two_occurrences_value = n_of_a_kind_value(2, count_values)
        return [7, three_occurrences_value, two_occurrences_value]
    else:
        return None
    
def check_flush(values, suits, count_values):
    return [6, max(values)] if is_same_suit(suits) else None

def check_straight(values, suits, count_values):
    if is_straight(values):
        return [9, max(values)]
    if values == [2, 3, 4, 5, 14]:
        return [9, 5]
    return None

def check_three_of_a_kind(values, suits, count_values):
    if n_of_a_kind(3, count_values):
        three_of_a_kind_value = n_of_a_kind_value(3, count_values)
        remaining_values = sorted([key for key, count in count_values.items() if key != three_of_a_kind_value], reverse=True)
        return [4, three_of_a_kind_value] + remaining_values
    return None

def check_two_pairs(values, suits, count_values):
    pairs = [key for key, value in count_values.items() if value == 2]
    if len(pairs) == 2:
        pairs.sort(reverse=True) 
        largest_pair = pairs[0]
        second_largest_pair = pairs[1]
        remaining_value = [key for key, value in count_values.items() if value == 1][0]
        return [3, largest_pair, second_largest_pair, remaining_value]
    return None

def check_one_pair(values, suits, count_values):
    pairs = [key for key, value in count_values.items() if value == 2]
    if len(pairs) == 1:
        pair_value = pairs[0]
        remaining_values = [key for key, value in count_values.items() if value == 1]
        remaining_values.sort(reverse=True)
        return [2, pair_value] + remaining_values
    return None

def check_high_card(values, suits, count_values):
    return [1] + values[::-1]

def evaluate(hand):
    values = [value(card[0]) for card in hand]
    suits = [card[1] for card in hand]
    values.sort()
    count_values = Counter(values)    
    hand_checks = [
        check_royal_flush,
        check_straight_flush,
        check_four_of_a_kind,
        check_full_house,
        check_flush,
        check_straight,
        check_three_of_a_kind,
        check_two_pairs,
        check_one_pair,
        check_high_card
    ]
    for check_func in hand_checks:
        result = check_func(values, suits, count_values)
        if result:
            return result

def main():
    player1_wins = 0
    player2_wins = 0
    num_lines = 0
    file_path = "MyPoker.txt"
    with open(file_path, 'r') as file:
        file_content = file.read()
        lines = file_content.split('\n')
        for line in lines:
            if len(line) == 0:
                break
            num_lines += 1
            hands = line.split()
            player1_hand = hands[:5]
            player2_hand = hands[5:]
            eval_1 = evaluate(player1_hand)
            eval_2 = evaluate(player2_hand)
            min_len = min(len(eval_1), len(eval_2))
            for i in range(min_len):
                if eval_1[i] > eval_2[i]:
                    player1_wins += 1
                    break
                elif eval_1[i] < eval_2[i]:
                    player2_wins += 1
                    break
    print(f"Player 1 wins: {player1_wins}")
    print(f"Player 2 wins: {player2_wins}")
    print(num_lines)
if __name__ == "__main__":
    main()