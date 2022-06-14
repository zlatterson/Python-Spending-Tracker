from datetime import datetime
from operator import attrgetter

# from controllers.item_controller import transaction

class Transaction:
    def __init__(self,merchant,user,item,cost,time=None,id=None,today=False):
        self.merchant = merchant
        self.user = user
        self.item = item
        self.cost = cost
        self.time = time
        self.id = id
        self.today = today
    
    def sort_by_user(transactions,userid):
        user_transactions = []
        for transaction in transactions:
            if transaction.user.id == userid:
                user_transactions.append(transaction)
        return user_transactions

    def sort_by_time(transactions):
        sorted_list = sorted(transactions, key=attrgetter('time'),reverse=True)
        return sorted_list

    def sort_by_month(transactions,year,month):
        # Filter by year
        by_year=[]
        for transaction in transactions:
            if transaction.time[0:4] == year:
                by_year.append(transaction)
                #  finds only those with the same year
        by_month=[]
        for transaction in by_year:
            if transaction.time[5:7] == month:
                by_month.append(transaction)
        return by_month

    def find_monthly_expendature(month_transactions):
        amount = 0
        for transaction in month_transactions:
            amount += transaction.item.cost
        return amount

    # Two functions with two varaibles, one will return None. To bypass pure HTML restrictions

    def green_text(month_cur,month_max):
        value = ""
        if month_cur < month_max:
            value = "{:,}".format(month_cur)
            value = "£"+str(month_cur)+"/"
        return value


    def red_text(month_cur,month_max):
        value = ""
        if month_cur > month_max:
            value = "{:,}".format(month_cur)
            value = "£"+str(value)+"/"
        return value


    def find_tag_total(tags):
        tags_total = 0
        for tag in tags:
            tags_total += tag.times_used
        return tags_total


    def change_transaction_object_tag_into_percentage(transactions,tag_total):
        for transaction in transactions:
            transaction.item.tag.times_used = round(transaction.item.tag.times_used / tag_total * 100)
        return transactions

    def check_if_date_condition(transactions,curdate):
        todays_date = curdate[0:10]

        for transaction in transactions:
            if transaction.time[0:10] == todays_date:
                transaction.today = True
        return transactions

    def format_money(transactions):
        for transaction in transactions:
            transaction.item.cost = "{:,}".format(transaction.item.cost)
        return transactions

# will return a list of transacitons, but only one per month
    def transaction_dates(transaction_list):
        transaction_dates = []
        for transaction in transaction_list:
            transaction_dates.append(transaction.time[0:7])
        
        remove_duplicates = list(dict.fromkeys(transaction_dates))
        replace_hyphons = []
        for transaction_date in remove_duplicates:
            replace_hyphons.append(transaction_date.replace('-', '/'))
        return replace_hyphons

        

        # {}
        # one_per_month = []
        # for transaction in transactions:
        #     if transaction.time[0:10] == transactions
        # else:
        #     one_per_month.append(transaction)
        