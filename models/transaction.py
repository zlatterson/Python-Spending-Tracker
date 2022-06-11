class Transaction:
    def __init__(self,merchant,user,item,cost,id=None):
        self.merchant = merchant
        self.user = user
        self.item = item
        self.cost = cost
        self.id = id