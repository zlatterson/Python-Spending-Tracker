class Transaction:
    def __init__(self,merchant,item,user,cost,id=None):
        self.merchant = merchant
        self.item = item
        self.user = user
        self.cost = cost
        self.id = id