'''
Card class represents the object of a game card
'''
class Card:
    name = ''
    kind = ''
    value = 0
    alternatValue=0
    points=0
    def __init__(self,id,name,kind,value,alternantValue,points):
      self.id=id
      self.name=name
      self.kind=kind
      self.value=value
      self.alternantValue=alternantValue
      self.points=points
