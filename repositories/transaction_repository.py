from unittest import result
from db.run_sql import run_sql

from models.merchant import Merchant
from models.transaction import Transaction

import repositories.merchant_repository as merchant_repository
import repositories.user_repository as user_repository
import repositories.item_repository as item_repository

def save(transaction):
    sql = "INSERT INTO transactions (merchant_id, user_id, item_id, cost) VALUES (%s,%s,%s,%s) RETURNING id"
    values = [transaction.merchant.id, transaction.user.id, transaction.item.id,transaction.cost]
    results = run_sql(sql,values)
    transaction.id = results[0]['id']
    return transaction

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for row in results:
        merchant = merchant_repository.select(row["merchant_id"])
        item = item_repository.select(row["item_id"])
        user = user_repository.select(row["user_id"])
        transaction = Transaction(merchant,user,item,row["cost"])
        transactions.append(transaction)
    return transactions

def select(id):
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        merchant = merchant_repository.select(result["merchant_id"])
        item = item_repository.select(result["item_id"])
        user = user_repository.select(result["user_id"])
        transaction = Transaction(merchant,user,item,result["cost"])
    return transaction

def update(transaction):
    sql = "UPDATE transactions SET (merchant_id, user_id, item_id, cost) = (%s,%s,%s,%s) WHERE id = %s"
    values = [transaction.merchant.id,transaction.user.id,transaction.item.id,transaction.cost,transaction.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)
