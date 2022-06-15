from operator import attrgetter


class Merchant:
    def __init__(self,name,money_received,id=None,received_percentage=None):
        self.name = name
        self.money_received = money_received
        self.id = id
        self.received_percentage = received_percentage
    

    def received_as_percentage(merchants):
        total = 0
        for merchant in merchants:
            total += merchant.money_received

        for merchant in merchants:
            merchant.received_percentage = round(merchant.money_received / total * 100)
        return merchants


    def order_merchants_by_spent(merchants):
        merchants.sort(key=lambda x: x.money_received, reverse=True)
        newlist = sorted(merchants, key=lambda x: x.money_received, reverse=True)

        top_5 = newlist[:5]
        return top_5
    
    def format_money(merchants):
        for merchant in merchants:
            merchant.money_received = "{:,}".format(merchant.money_received)
        return merchants