from db.run_sql import run_sql

from models.merchant import Merchant

import repositories.merchant_repository as merchant_repository
import repositories.user_repository as user_repository
import repositories.item_repository as item_repository

def save(transaction):
    sql = "INSERT INTO transactions (merchant_id, item_id, user_id, cost) VALUES (%s,%s,%s,%s) RETURNING id"
    values = [transaction.merchant.id,transaction.item.id, transaction.user.id, transaction.cost]
    results = run_sql(sql,values)
    transaction.id = results[0]['id']
    return transaction