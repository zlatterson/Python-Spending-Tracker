from db.run_sql import run_sql

from models.user import User

def save(user):
    sql = "INSERT INTO users (name,money,daily_allowance) VALUES (%s,%s,%s) RETURNING id"
    values = [user.name, user.money, user.daily_allowance]
    results = run_sql(sql,values)
    user.id = results[0]['id']
    return user

def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        user = User(row["name"],row["money"],row["daily_allowance"],row["id"])
        users.append(user)
    return users

def select(id):
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    user = User(result["name"],result["money"],result["daily_allowance"],result["id"])
    return user


def update(user):
    sql = "UPDATE users SET (name, money, daily_allowance) = (%s,%s,%s) WHERE id = %s"
    values = [user.name,user.money,user.daily_allowance,user.id]
    run_sql(sql,values)

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)