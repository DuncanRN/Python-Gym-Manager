# from collections import UserString
# from msilib.schema import Class
from db.run_sql import run_sql
# from models.booking import Booking
from models.member import Member
from models.class import Class
# the colours aren't right there, but I think that is ok...?

def save(member):
    sql = "INSERT INTO members(first_name, last_name) VALUES ( %s, %s ) RETURNING id"
    values = [member.first_name, member.last_name]
    results = run_sql( sql, values )
    member.id = results[0]['id']
    return member

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row['first_name'], row['last_name'], row['id'])
        members.append(member)
    return members


def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['id'] )
    return member

def classes(member):
    classes = []
    sql = "SELECT classes.* FROM classes INNER JOIN bookings ON bookings.class_id = classes.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        class = Class(row['id'], row['name'])
        classes.append(class)
    return classes



def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

