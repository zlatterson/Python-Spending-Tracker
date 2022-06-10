from db.run_sql import run_sql

from models.item import Item
# import merchant?

def save(item):
    sql = "INSERT INTO items (name,tag,cost,merchant_id) VALUES (%s,%s,%s,%s) RETURNING id"
    values = [item.name, item.tag, item.cost, item.merchant.id]
    results = run_sql(sql,values)
    item.id = results[0]['id']
    return item