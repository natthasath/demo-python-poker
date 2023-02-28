import random
import collections

class Card:
    def __init__(self):
        self._suits = ['club', 'diamond', 'heart', 'spade']
        self._ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

    def get_suits(self):
        return self._suits

    def get_ranks(self):
        return self._ranks

    """def get_royal(self, p):
        count = 0
        obj = Card.get_index(self, p)
        royal = [8, 9, 10, 11, 12]
        if obj == royal:
            count += 1            
        return (count == 1 and True or False)"""

class Deck(Card):
    def __init__(self):
        super().__init__()
        self._deck = []

    def set_deck(self):
        for k in range(0, len(self._ranks)):            
            for j in range(0, len(self._suits)):
                r = self._ranks[k]
                s = self._suits[j]
                d = r + ' ' + s
                self._deck.append(d)
        return self._deck

    def get_deck(self):
        return self._deck

    def get_draw(self):
        draw = random.choice(self._deck)
        self._deck.remove(draw)
        return draw

    def get_index(self):
        obj = []
        for k in range(0, len(self._deck)):       
            index = self._deck.index(self._deck[k])
            obj.append(index)
        obj.sort()
        return obj

class Score(Deck):
    def __init__(self):
        super().__init__()

    """def high(self):
        count = 0
        return '9'"""
        
    def pair(self, hold):
        count = 0
        arr = []
        #obj = list(collections.Counter(hold).items())
        for line in hold:
            arr.append(line[0])
            print(arr)
            """if line[1] == 2:
                count += 1
        return (count == 1 and True or '8')"""

    """def two_pair(self):
        count = 0
        obj = list(collections.Counter(self._p2).items())
        for line in obj:
            if line[1] == 2:
                count += 1
        return (count == 2 and True or '7')

    def trips(self):
        count = 0
        obj = list(collections.Counter(self._p2).items())
        for line in obj:
            if line[1] == 3:
                count += 1
        return (count == 1 and True or '6')

    def straight(self, p2):
        count = 0
        obj = Draw.get_index(self, self._p2)
        for k in range(0, len(obj)):
            if k != 0:
                if obj[k] == obj[k - 1] + 1:
                    count += 1
            else:
                count += 1
        return (count == 5 and True or '5')

    def flush(self):
        count = len(self._p1)
        obj = list(collections.Counter(self._p1).items())
        return (obj == [(self._p1[0], count)] and True or '4')

    def fullhouse(self):
        count_pair = 0
        count_trips = 0
        obj = list(collections.Counter(self._p2).items())
        for line in obj:
            if line[1] == 2:
                count_pair += 1
            elif line[1] == 3:
                count_trips += 1
        return ((count_pair == 1 and count_trips == 1) and True or '3')

    def quads(self):
        count = 0
        obj = list(collections.Counter(self._p2).items())
        for line in obj:
            if line[1] == 4:
                count += 1
        return (count == 1 and True or '2')

    def straight_flush(self):
        count = 0
        flush = Score.flush(self)
        straight = Score.straight(self)
        if flush == True and straight == True:
            count += 1        
        return (count == 1 and True or '1')

    def royal_straight_flush(self):
        count = 0
        flush = Score.flush(self)
        straight = Score.straight(self)
        royal = Card.get_royal(self, self._p2)
        if flush == True and straight == True and royal == True:
            count += 1
        return (count == 1 and True or '0')"""

def Board(card):
    s = Score()
    score = ''
    score = s.pair(card)
    """if score == '':
        score = s.straight_flush()
    elif score == '1':
        score = s.quads()
    elif score == '2':
        score = s.fullhouse()
    elif score == '3':
        score = s.flush()
    elif score == '4':
        score = s.straight()
    elif score == '5':
        score = s.trips()
    elif score == '6':
        score = s.two_pair()
    elif score == '7':
        score = s.pair()
    elif score == '8':
        score = s.high()"""
    
    return score

def Play():
    d = Deck()
    d.set_deck()
    p1 = []
    p2 = []
    count = 0
    flop = [''] * 5
    carryOn = 'Y'    
    for k in range(0, 3):
        f = d.get_draw()
        flop[count] = f
        p1.append(f)
        p2.append(f)
        count += 1
    print(flop)
    while carryOn.upper() == 'Y':
        if len(p1) < 5:
            p1.append(d.get_draw())
            p2.append(d.get_draw())
        elif len(p1) < 7:
            f = d.get_draw()
            flop[count] = f
            p1.append(f)
            p2.append(f)
            count += 1
            carryOn = input('Do you want to draw (Y/N): ? ')
            print('{0:15} {1:15} {2:15} {3:15} {4:15}'.format(flop[0], flop[1], flop[2], flop[3], flop[4]))
        else:
            break
    b1 = Board(p1)
    print(p1)
    print(b1)
    
def main():
    Play()
    #Board()
    #s = Score()
    #print(s.royal_straight_flush())

main()
