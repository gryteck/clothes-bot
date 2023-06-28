class Card:
    def __init__(self, start_rate):
        self.card = start_rate

    def upd(self, new_card):
        self.card = new_card
        return self.card

    def get(self):
        return self.card


rate = Card("")
