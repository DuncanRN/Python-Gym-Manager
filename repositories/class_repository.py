from db.run_sql import run_sql
from models.class import Class
from models.member import Member

def save(class):
    sql = "INSERT INTO classes ( name ) VALUES ( %s ) RETURNING id"
    values = [class.name]
    results = run_sql( sql, values )
    class.id = results[0]['id']
    return class

def select_all():
    classes = []

    sql = "SELECT * FROM classes"
    results = (sql)

    for row in results:
        class = Class(row['name'], row['id']  )
        classes.append(class)
    return classes



def select(id):
    class = None
    sql = "SELECT * FROM classes where id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        class = Class(results['name'], result['id'])
    return class


# are we using this next method?
def members(class):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE class_id = %s;"
    values = [class.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['first_name'], row['last_name'], row['id'])
        members.append(member)
    return members


def delete_all():
    sql = "DELETE FROM classes"
    run_sql(sql)
    