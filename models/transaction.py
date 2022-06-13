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

    def sort_by_time(transactions,time=None):
        # # sorted_by_date = []
        # datetime_object = datetime.strptime(transactions.time)
        # sort = sorted(datetime_object)
        # # sort = transactions.time.sort(key=lambda date: time(date, "%d/%m/%Y %H:%M:%S"))

        # transaction_time = []
        # for transaction in transactions:
        #     transaction_time.append(transaction.time)
        # sort_times = sorted(transaction_time)

        # sorted_list = transactions.sort(key=lambda r: r.time)
        sorted_list = sorted(transactions, key=attrgetter('time'))

        # sorted_list = sorted(transactions,key=lambda k: datetime.strptime(k['time'], '%Y-%m-%d %I:%M:%S %p'),reverse=False)



        return sorted_list
