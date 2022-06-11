from db.run_sql import run_sql

from models.item import Item
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

def save(item):
    sql = "INSERT INTO items (name,cost,tag_id,merchant_id) VALUES (%s,%s,%s,%s) RETURNING id"
    values = [item.name, item.cost,item.tag.id, item.merchant.id]
    results = run_sql(sql,values)
    item.id = results[0]['id']
    return item

def select_all():
    items = []
    sql = "SELECT * FROM items"
    results = run_sql(sql)
    for row in results:
        merchant = merchant_repository.select(row["merchant_id"])
        tag = tag_repository.select(row["tag_id"])
        item = Item(row["name"],row["cost"],tag,merchant,row["id"])
        items.append(item)
    return items

def select(id):
    sql = "SELECT * FROM items WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        merchant = merchant_repository.select(result["merchant_id"])
        tag = tag_repository.select(result["tag_id"])
        item = Item(result["name"],result["cost"],tag,merchant,result["id"])
    return item


def delete_all():
    sql = "DELETE FROM items"
    run_sql(sql)

def update(item):
    sql = "UPDATE items SET (name,cost,tag_id,merchant_id) = (%s,%s,%s,%s) WHERE id = %s"
    values = [item.name, item.cost,item.tag.id, item.merchant.id, item.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM items WHERE id = %s"
    values = [id]
    run_sql(sql, values)
