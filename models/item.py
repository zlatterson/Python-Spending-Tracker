class Item:
    def __init__(self,name,tag,cost,merchant,id=None):
        self.name = name
        self.tag = tag
        self.cost = cost
        self.merchant = merchant
        self.id = id