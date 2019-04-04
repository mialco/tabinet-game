'''
card_attributes.py
A class containing mapping of the card attributes identifiers to human readble names
Example card signs 1 =  Clubs 2. Diamond 3. Heart 4 spade
'''
class CardAttributes:

    tabinet_card_set = { 
    1 :  {'name': 'ace', 'value' : 1, 'alternant_value' : 11, 'points': 1  }
    ,2 : {'name': 'two', 'value' : 2, 'alternant_value' : 0, 'points': 0  } 
    ,3 : {'name': 'three', 'value' : 3, 'alternant_value' : 0, 'points': 0  } 
    ,4 : {'name': 'four', 'value' : 4, 'alternant_value' : 0, 'points': 0  } 
    ,5 : {'name': 'five','value' : 5, 'alternant_value' : 0, 'points': 0  } 
    ,6 : {'name': 'six','value' : 6, 'alternant_value' : 0, 'points': 0  } 
    ,7 : {'name': 'seven','value' : 7, 'alternant_value' : 0, 'points': 0  } 
    ,8 : {'name': 'eigth','value' : 8, 'alternant_value' : 0, 'points': 0  } 
    ,9 : {'name': 'nine','value' : 9, 'alternant_value' : 0, 'points': 0  } 
    ,10 : {'name': 'ten','value' : 10, 'alternant_value' : 0, 'points': 1  } 
    ,11 : {'name': 'jack','value' : 12, 'alternant_value' : 0, 'points': 1  } 
    ,12 : {'name': 'queen','value' : 13, 'alternant_value' : 0, 'points': 1  } 
    ,13 : {'name': 'king','value' : 14, 'alternant_value' : 0, 'points': 1  } 
    }

    card_kinds = {1: 'spade', 2: 'heart', 3: 'diamond' , 4 : 'club'  }


    