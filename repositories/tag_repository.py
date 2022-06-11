from db.run_sql import run_sql

from models.tag import Tag

def save(tag):
    sql = "INSERT INTO tags (name,times_used) VALUES (%s,%s) RETURNING id"
    values = [tag.name, tag.times_used]
    results = run_sql(sql,values)
    tag.id = results[0]['id']
    return tag


def select_all():
    tags = []
    sql = "SELECT * FROM tags"
    results = run_sql(sql)
    for row in results:
        tag = Tag(row["name"],row["times_used"],row["id"])
        tags.append(tag)
    return tags

def select(id):
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    if result is not None:
        tag = Tag(result["name"],result["times_used"],result["id"])
    return tag

def update(tag):
    sql = "UPDATE tags SET (name, times_used) = (%s,%s) WHERE id = %s"
    values = [tag.name, tag.times_used, tag.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)