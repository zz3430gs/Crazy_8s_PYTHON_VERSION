"""This Class creates a fresh deck of cards every time it is called."""
import random
class deck_of_cards:
    dict_of_values={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':50,'9':9,'10':10,'J':10,'Q':10,'K':10}
    suits=['Hearts','Spades','Clubs','Diamonds']
    numbers_and_faces=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    """ This class has a single inner class.  For the sake of compartmentalization I have put it here instead of its own file."""
    class card:
        def __init__(self,suit,face_or_number):
            self.suit=suit
            self.face_or_number=face_or_number
        # representaion when printed, javas toString override
        def __repr__(self):
            self.str_rep=self.face_or_number+' of '+ self.suit
            return self.str_rep
    def __init__(self):

        self.deck=[]
        # For every thing in the lists make a deck
        for suit in self.suits:
            i=suit
            for number_or_face in self.numbers_and_faces:
                j=number_or_face
                self.deck.append(deck_of_cards.card(i,j))
        random.shuffle(self.deck)

    def print_whole_deck(self):
        for card in self.deck:
            print(card)
    def deal_a_card_to_player_hand(self):
        # this method deals from the bottom of the deck ( I know that's not legal techinically but whatever)
        try:
            a_card = self.deck.pop()
            return a_card
        except IndexError:
            "The game experienced an unexpected error! There were no cards left!"