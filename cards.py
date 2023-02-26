import random



_ranks = ["J", "K", "Q", "A", 6, 7, 8, 9, 10]
_suits = ['\u2660',
         '\u2665',
         '\u2666',
         '\u2663']

class Game():
    def __init__(self):
        self.r=random.choice(_ranks)
        self.s=random.choice(_suits)

    def __repr__(self):
        return f'{self.r}{self.s}'

    def divination():
        card=Game()


        yourquestion=input("Про що ти хочеш дізнатись?")

        if card.r == ("A") or card.r == ("K") and card.s == {'\u2660'} or card.s == {'\u2665'}:
            print(f"Вам випала карта {card.__repr__()} Ваше питання вирішиться ПОЗИТИВНО!")
            
        elif card.r == ("Q") or card.r == ("J") and card.s == {'\u2666'} or card.s == {'\u2663'}:
            print(f"Вам випала карта {card.__repr__()} Можливі перешкоди, але все буде добре!")
            
        elif card.r == (7) or card.r == (8) or card.r == (9) or card.r == (10) and card.s == {'\u2660'} or card.s == {'\u2666'}:
            print(f"Вам випала карта {card.__repr__()} Ситуація важка, але надія є!")
            
        else:
            print(f"Вам випала карта {card.__repr__()} Вибачте, але це поганий результат!")
            
            

        
if __name__ == '__main__':
    Game()
