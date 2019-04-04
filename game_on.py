from cards import card_manager

def start():
    print ('Starting ceremonies')
    cm = card_manager.CardManager()
    cm.generate_deck()
    pass



if __name__ == '__main__':
    start()
