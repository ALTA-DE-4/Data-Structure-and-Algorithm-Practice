def playing_domino(cards, deck):
  for card in cards:
    if card[0] in deck or card[1] in deck:
      return card
  return []

print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))
print(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]))
print(playing_domino([[6, 6], [2, 4], [3, 16]], [5, 1]))