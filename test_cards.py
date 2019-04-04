import unittest
from cards import card_manager

class TestCards(unittest.TestCase):

    '''We are buiilding a card deck and we are supposed to find all 52 cards
    '''
    def test_tabinet_card_deck(self):
        cm= card_manager.CardManager()
        cm.generate_deck()
        counter=0
        points=0
        values=0
        alternantValues=0
        for item in cm.main_deck:
            counter+=1
            values+=item.value
            points+=item.points
            alternantValues+=item.alternantValue
        self.assertEqual(len(cm.main_deck),52)
        self.assertEqual(values,376)
        self.assertEqual(alternantValues,44)
        self.assertEqual(points,21)
if __name__ == '__main__':
    unittest.main()    