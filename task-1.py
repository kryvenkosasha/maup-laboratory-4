def choose_pile(piles):
    max_pile = max(piles)
    pile_number = piles.index(max_pile) + 1
    return pile_number

coins = input("введите количество монет в куче ")
piles = list(map(int, coins.split()))

if len(piles) == 3:
    best_pile = choose_pile(piles)
    print(best_pile)
