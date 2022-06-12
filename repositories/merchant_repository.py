from db.run_sql import run_sql

from models.merchant import Merchant

def save(merchant):
    sql = "INSERT INTO merchants (name,money_received) VALUES (%s,%s) RETURNING id"
    values = [merchant.name, merchant.money_received]
    results = run_sql(sql,values)
    merchant.id = results[0]['id']
    return merchant


def select_all():
    merchants = []
    sql = "SELECT * FROM merchants"
    results = run_sql(sql)
    for row in results:
        merchant = Merchant(row["name"],row["money_received"],row["id"])
        merchants.append(merchant)
    return merchants

def select(id):
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    if result is not None:
        merchant = Merchant(result["name"],result["money_received"],result["id"])
    return merchant


def update(merchant):
    sql = "UPDATE merchants SET (name, money_received) = (%s,%s) WHERE id = %s"
    values = [merchant.name,merchant.money_received, merchant.id]
    run_sql(sql,values)

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)
