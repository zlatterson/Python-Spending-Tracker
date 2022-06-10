import pdb
from models.item import Item
from models.merchant import Merchant
from models.user import User

import repositories.user_repository as user_repository
import repositories.merchant_repository as merchant_repository
import repositories.item_repository as item_repository

user_repository.delete_all()
merchant_repository.delete_all()
item_repository.delete_all()

user1 = User("Todd",10,20)
user_repository.save(user1)

user2 = User("Timmy",1000, 30)
user_repository.save(user2)
# 
users = user_repository.select_all()
for user in users:
    print (user.id, user.name, user.money)
# pass: select all working

selected_user = user_repository.select(user1.id)
print (selected_user.name, selected_user.id)
# pass: select user working

user1 = User("Todd",3000,50,user1.id)
user_repository.update(user1)

users = user_repository.select_all()
for user in users:
    print (user.id, user.name, user.money)
# pass: user update

user_repository.delete(user1.id)

users = user_repository.select_all()
for user in users:
    print (user.id, user.name, user.money)
# pass: delete specific user


# ____________________MERCHANTS_____
merchant1 = Merchant("Amazon",10)
merchant_repository.save(merchant1)
print (merchant1.id, merchant1.name, merchant1.money_received)

merchant2 = Merchant("Alibaba",20)
merchant_repository.save(merchant2)

merchant1 = Merchant("Amazon",1000,merchant1.id)
merchant_repository.update(merchant1)

merchants = merchant_repository.select_all()
for merchant in merchants:
    print (merchant.id, merchant.name, merchant.money_received)

# _______ITEMS___
print(merchant1.id)
item1= Item("ball","toy",10,merchant1)
item_repository.save(item1)

item2= Item("yoyo","toy",5,merchant1)
item_repository.save(item2)

items = item_repository.select_all()
for item in items:
    print(item.name, item.id, item.merchant.name, item.tag, item.cost)

specific_item = item_repository.select(item2.id)
print(specific_item.name, specific_item.id, specific_item.merchant.name, specific_item.cost)

# specific item working

item2= Item("yoyo","weapon",10,merchant2,item2.id)
item_repository.update(item2)

items = item_repository.select_all()
for item in items:
    print(item.name, item.id, item.merchant.name, item.tag, item.cost)
    print(item.merchant.id)



pdb.set_trace()