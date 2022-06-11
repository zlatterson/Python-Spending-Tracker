import pdb
from models.item import Item
from models.merchant import Merchant
from models.user import User
from models.transaction import Transaction
from models.tag import Tag

import repositories.user_repository as user_repository
import repositories.merchant_repository as merchant_repository
import repositories.item_repository as item_repository
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository

user_repository.delete_all()
merchant_repository.delete_all()
item_repository.delete_all()
transaction_repository.delete_all()
tag_repository.delete_all()

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

# ____TAGS___
tag1 = Tag("sword",20)
tag_repository.save(tag1)

tag2 = Tag("shield",0)
tag_repository.save(tag2)

tag3 = Tag("toy",0)
# tag save works

all_tags = tag_repository.select_all()
for tag in all_tags:
    print(tag.id, tag.name, tag.times_used)

# tag select all: works

specific_tag = tag_repository.select(tag2.id)
print(specific_tag.id,specific_tag.name,specific_tag.times_used)

# tag select one: works

tag1 = Tag("sword",0,tag1.id)
tag_repository.update(tag1)

all_tags = tag_repository.select_all()
for tag in all_tags:
    print(tag.id, tag.name, tag.times_used)
# tag update: works

# print("test delete:")
# tag_repository.delete(tag1.id)
# all_tags = tag_repository.select_all()
# for tag in all_tags:
#     print(tag.id, tag.name, tag.times_used)
# # single delete: works

# _______ITEMS___
print(merchant1.id)
item1= Item("buckle shield",10,tag1,merchant1)
item_repository.save(item1)

item2= Item("yoyo",20,tag2,merchant1)
item_repository.save(item2)

items = item_repository.select_all()
for item in items:
    print(item.id, item.name, item.cost, item.tag.name, item.tag.times_used, item.merchant.name, item.cost)
    print(item.merchant, item.tag)
# select all: working

specific_item = item_repository.select(item2.id)
print(specific_item.name, specific_item.id, specific_item.tag.name, specific_item.merchant.name, specific_item.cost)

 # specific item working
print("test update:")
items = item_repository.select_all()
for item in items:
    print(item.name, item.id, item.merchant.name, item.tag.name, item.cost)

item2= Item("yoyo",50,tag1,merchant2,item2.id)
item_repository.update(item2)

print("new values:")
items = item_repository.select_all()
for item in items:
    print(item.name, item.id, item.merchant.name, item.tag.name, item.cost)
# update working
# # ____________________TRANSACTIONS_________________

users = user_repository.select_all()
for user in users:
    print("id is")
    print(user.id, user.name)


transaction1 = Transaction(merchant1,user2,item2,item2.cost)
transaction_repository.save(transaction1)

transaction2 = Transaction(merchant1,user2,item1,item1.cost)
transaction_repository.save(transaction2)

# # -- save transactions: working

transaction_list = transaction_repository.select_all()
for transaction in transaction_list:
    print(transaction.merchant.name, transaction.item.name, transaction.user.name, transaction.cost)

# # -- select all transactions: working

print(transaction1.id)
single_transaction = transaction_repository.select(transaction2.id)
print(single_transaction.id, single_transaction.cost, single_transaction.merchant.name, single_transaction.user.name)
# # -- select single transaction: working
transaction_list = transaction_repository.select_all()
print("before testing update:")
for transaction in transaction_list:
    print(transaction.merchant.name, transaction.item.name, transaction.user.name, transaction.cost)

tuser = User("Brian",1000,60)
user_repository.save(tuser)

tmerchant = Merchant("McDonalds",10)
merchant_repository.save(tmerchant)

ttag = Tag("burger",1)
tag_repository.save(ttag)

titem= Item("Big Mac",10,ttag,tmerchant)
item_repository.save(titem)


transaction1 = Transaction(tmerchant,tuser,titem,titem.cost,transaction1.id)
transaction_repository.update(transaction1)

transaction_list = transaction_repository.select_all()
print("testing update:")
for transaction in transaction_list:
    print(transaction.merchant.name, transaction.item.name, transaction.item.tag.name, transaction.user.name, transaction.cost)
# # -- transaction update: working

transaction_repository.delete(transaction2.id)
transaction_list = transaction_repository.select_all()
for transaction in transaction_list:
    print(transaction.merchant.name, transaction.item.name, transaction.item.tag, transaction.user.name, transaction.cost)
# # delete single transaction: working




pdb.set_trace()