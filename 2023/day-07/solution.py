from functools import cmp_to_key

with open('input.txt') as f:
    lines = f.readlines()

hands = [line.rstrip().split(' ') for line in lines]

card_rank = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

FIVE_OF_A_KIND = 0
FOUR_OF_A_KIND = 1
FULL_HOUSE = 2
THREE_OF_A_KIND = 3
TWO_PAIR = 4
ONE_PAIR = 5
HIGH_CARD = 6


def get_hand_rank(hand):
    unique = set(hand)
    card_count = [hand.count(u) for u in unique]

    if len(unique) == 1:  # Five of a Kind
        return FIVE_OF_A_KIND

    elif len(unique) == 2:  # Four of a Kind, Full House, Three of a Kind
        if 4 in card_count:
            return FOUR_OF_A_KIND
        elif 2 in card_count and 3 in card_count:
            return FULL_HOUSE
        elif 3 in card_count:
            return THREE_OF_A_KIND

    elif len(unique) == 3:  # Two Pair or Three of a Kind
        if 3 in card_count:
            return THREE_OF_A_KIND
        return TWO_PAIR

    elif len(unique) == 4:  # One Pair
        return ONE_PAIR

    else:
        return HIGH_CARD


def make_compare(include_jokers=False):
    def compare(hand1, hand2):
        hand1, hand2 = hand1[0], hand2[0]

        hand1_rank = get_hand_rank(hand1)
        hand2_rank = get_hand_rank(hand2)

        if include_jokers:
            hand1_rank = min([get_hand_rank(hand1[:].replace("J", u)) for u in set(hand1)])
            hand2_rank = min([get_hand_rank(hand2[:].replace("J", u)) for u in set(hand2)])

        if hand1_rank != hand2_rank:
            return hand2_rank - hand1_rank

        for i, card1 in enumerate(hand1):
            rank1 = card_rank.index(card1)
            card2 = hand2[i]
            rank2 = card_rank.index(card2)
            if card1 != card2:
                return rank2 - rank1
        return 0

    return compare


def get_winnings(rankings):
    for i, rank in enumerate(rankings):
        print(f"{i}: {rank}")
    return sum([(rank + 1) * int(bet) for rank, [_, bet] in enumerate(rankings)])


part1 = get_winnings(sorted(hands, key=cmp_to_key(make_compare())))

print(f"Part 1: {part1}")

# Part 2
card_rank.remove('J')

part2 = get_winnings(sorted(hands, key=cmp_to_key(make_compare(True))))

print(f"Part 2: {part2}")
