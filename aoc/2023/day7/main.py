from collections import defaultdict

def main():
    with open("input", "r") as f:
        input_bids = f.read().splitlines()

    bids = parse_bids(input_bids)
    result = total_winnings(bids)

    print(result)

def run_tests():
    input_bids = [
        "32T3K 765",
        "T55J5 684",
        "KK677 28",
        "KTJJT 220",
        "QQQJA 483"
    ]

    bids = parse_bids(input_bids)
    result = total_winnings(bids)

    print(result)
    assert result == 6440

def parse_bids(lines):
    bids = {}
    for l in lines:
        hand, bid = l.split(" ")
        bids[hand] = int(bid)
    return bids

def rank_hand(hand):
    counts = defaultdict(int)
    for card in hand:
        counts[card] += 1

    counts_of_counts = defaultdict(int)
    for count in counts.values():
        counts_of_counts[count] += 1

    by_cards = rank_hand_by_cards(hand)

    rank = 0
    if counts_of_counts[5] == 1:
        rank = 6
    elif counts_of_counts[4] == 1:
        rank = 5
    elif counts_of_counts[3] == 1 and counts_of_counts[2] == 1:
        rank = 4
    elif counts_of_counts[3] == 1:
        rank = 3
    elif counts_of_counts[2] == 2:
        rank = 2
    elif counts_of_counts[2] == 1:
        rank = 1
    else:
        rank = 0

    return f"0x{rank:x}{by_cards}"

CARDS_ORDER = {c:hex(i) for i, c in enumerate(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"][::-1])}

def rank_hand_by_cards(hand):
    return ''.join([CARDS_ORDER[c][2:] for c in hand])

def total_winnings(bids):
    ranks = {}
    for b in bids:
        ranks[b] = rank_hand(b)

    winnings = [] 
    for r, b in enumerate(sorted(bids.keys(), key=lambda x: ranks[x])):
        winnings.append((r + 1) * bids[b])
    return sum(winnings)


if __name__ == "__main__":
    main()

