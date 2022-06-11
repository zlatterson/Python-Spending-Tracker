class Item:
    def __init__(self,name,cost,tag,merchant,id=None):
        self.name = name
        self.cost = cost
        self.tag = tag
        self.merchant = merchant
        self.id = id