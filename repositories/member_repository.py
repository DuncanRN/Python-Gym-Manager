# import pdb
# from collections import UserString
# from msilib.schema import Class
from db.run_sql import run_sql
# from models.booking import Booking
from models.member import Member
from models.gym_class import GymClass
# the colours aren't right there, but I think that is ok...?

def save(member):
    sql = "INSERT INTO members (first_name, last_name, membership, active) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [member.first_name, member.last_name, member.membership, member.active]
    print(sql)
    print(values)
    results = run_sql( sql, values )
    member.id = results[0]['id']
    return member

def update(member):
    # pdb.set_trace()
    sql = "UPDATE members SET (first_name, last_name, membership, active) = (%s, %s, %s, %s) WHERE id = %s"
    if(member.active=="True"):
        active=True
    else:
        active=False

    values = [member.first_name, member.last_name, member.membership, active,  member.id]
    print(sql)
    print(values)

    run_sql(sql, values)

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row['first_name'], row['last_name'], row['membership'],  row['active'], row['id'])
        members.append(member)
    return members


def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]

    print(sql)
    print(values)

    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['membership'], result['active'], result['id'] )
    return member

def gym_classes(member_id):
    gym_classes = []
    sql = "SELECT gym_classes.* FROM gym_classes INNER JOIN bookings ON bookings.gym_class_id = gym_classes.id WHERE member_id = %s"
    # THIS WORKS Leave it!
    
    
    values = [member_id]
    results = run_sql(sql, values)

    for row in results:
        gym_class = GymClass(row['name'], row['date_start'], row['repeating'], row['end_date'], row['capacity'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

