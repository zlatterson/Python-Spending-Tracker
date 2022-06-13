from datetime import datetime
from operator import attrgetter

# from controllers.item_controller import transaction

class Transaction:
    def __init__(self,merchant,user,item,cost,time=None,id=None):
        self.merchant = merchant
        self.user = user
        self.item = item
        self.cost = cost
        self.time = time
        self.id = id
    
    def sort_by_user(transactions,userid):
        user_transactions = []
        for transaction in transactions:
            if transaction.user.id == userid:
                user_transactions.append(transaction)
        return user_transactions

    def sort_by_time(transactions):
        sorted_list = sorted(transactions, key=attrgetter('time'),reverse=True)
        return sorted_list
