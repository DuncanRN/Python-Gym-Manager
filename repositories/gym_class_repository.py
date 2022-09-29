import pdb
from db.run_sql import run_sql
from models.gym_class import GymClass
from models.member import Member

def save(gym_class):
    sql = "INSERT INTO gym_classes ( name , date_start , repeating , end_date , capacity, status) VALUES ( %s , %s, %s, %s, %s, %s) RETURNING id"
    values = [gym_class.name, gym_class.date_start, gym_class.repeating, gym_class.end_date, gym_class.capacity, gym_class.status]
    results = run_sql( sql, values )
    gym_class.id = results[0]['id']
    return gym_class

def update(gym_class):
    sql = "UPDATE gym_classes SET name = %s, date_start = %s, repeating = %s, end_date = %s, capacity = %s, status = %s WHERE id = %s"
    values = [gym_class.name, gym_class.date_start, gym_class.repeating, gym_class.end_date, gym_class.capacity, gym_class.status,  gym_class.id]
    run_sql(sql, values)

def select_all():
    gym_classes = []

    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)

    for row in results:
        gym_class = GymClass(row['name'], row['date_start'], row['repeating'], row['end_date'], row['capacity'], row['status'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes


def select(id):
    gym_class = None
    sql = "SELECT * FROM gym_classes where id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        gym_class = GymClass(result['name'], result['date_start'], result['repeating'], result['end_date'], result['capacity'], result['status'], result['id'])
    return gym_class


def members(gym_class_id):
    members = []
    
    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE gym_class_id = %s"
    
    values = [gym_class_id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['first_name'], row['last_name'], row['membership'], row['active'], row['id'])
        members.append(member)
    return members

def members_not_in_class(gym_class_id):
    members = []
    
    sql = "SELECT members.* FROM members WHERE id NOT IN (SELECT members.id FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE gym_class_id = %s )"
    
    values = [gym_class_id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['first_name'], row['last_name'], row['membership'], row['active'], row['id'])
        members.append(member)
    return members

def delete_all():
    sql = "DELETE FROM gym_classes"
    run_sql(sql)
    

