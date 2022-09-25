from db.run_sql import run_sql
from models.gym_class import GymClass
from models.member import Member

def save(gym_class):
    sql = "INSERT INTO gym_classes ( name ) VALUES ( %s ) RETURNING id"
    values = [gym_class.name]
    results = run_sql( sql, values )
    gym_class.id = results[0]['id']
    return gym_class

def select_all():
    gym_classes = []

    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)

    for row in results:
        gym_class = GymClass(row['name'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes


def select(id):
    gym_class = None
    sql = "SELECT * FROM gym_classes where id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        gym_class = GymClass(result['name'],  result['id'])
    return gym_class


# are we using this next method?
def members(gym_class_id):
    members = []
    
    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE gym_class_id = %s"
    
    values = [gym_class_id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['first_name'], row['last_name'], row['id'])
        members.append(member)
    return members

def delete_all():
    sql = "DELETE FROM gym_classes"
    run_sql(sql)
    