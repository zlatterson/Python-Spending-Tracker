class User:
    def __init__(self,name,money,daily_allowance,id=None):
        self.name = name
        self.money = money
        self.daily_allowance = daily_allowance
        self.id = id

    def format_money(user):
        user.money = "{:,}".format(user.money)
        return user

    
    def format_monthly_allowance(user):
        user.daily_allowance = "{:,}".format(user.daily_allowance)
        return user
