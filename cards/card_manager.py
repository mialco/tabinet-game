'''
card_manager.py
A class that will manage the cards collections in the game
and it will serve the diferent functionalities related to the cards withing the game
It will provide functions like :
    Create the initial deck of cards
    Shuffle the deck of cards
    Serve cards from the different collections of cards 
    Allow access to the user to the proper collection of cards
'''
from cards import card
from cards import card_attributes

class CardManager:
    def __init__(self):
        self.main_deck=[]
    

    def generate_deck(self):
        '''Generates the main deck of cards
        '''    
        counter=0
        cn= card_attributes.CardAttributes.tabinet_card_set
        ck= card_attributes.CardAttributes.card_kinds
        for i in range (1,14):
            for j in range(1,5):
                counter+=1
                acard = card.Card(counter,cn[i]['name'],ck[j],cn[i]['value'],cn[i]['alternant_value'],cn[i]['points'])
                if acard.name =='two' and acard.kind=='club':
                    acard.points=1
                self.main_deck.append(acard)
            #add a point for the card two of club
    
    def shuffle_deck (self):
        