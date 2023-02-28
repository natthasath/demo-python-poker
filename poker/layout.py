rank = ["♣", "♦", "♥", "♠"]
suit = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def getLayout(suit, rank):
    card = []
    card.append('┌─────────┐')
    card.append('│{0:9}│'.format(rank[0]))
    card.append('│         │')
    card.append('│         │')
    card.append('│{0:^9}│'.format(suit[0]))
    card.append('│         │')
    card.append('│         │')
    card.append('│{0:>9}│'.format(rank[0]))
    card.append('└─────────┴')
    return card
   
data_1 = getLayout(suit, rank)
data_2 = getLayout(suit, rank)
    
for x in range(9):
    print(data_1[x], data_2[x])
