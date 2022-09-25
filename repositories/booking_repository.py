from db.run_sql import run_sql
from models.booking import Booking

def save(booking):
    sql = "INSERT INTO bookings ( member_id, gym_class_id) VALUES ( %s, %s) RETURNING id"
    values = [booking.member_id, booking.gym_class_id]   

    results = run_sql( sql, values )
    booking.id = results[0]['id']
    return booking


# not convinced that we are using this method
def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        booking = Booking(row['member_id'], row['gym_class_id'], row['id'])
        bookings.append(booking)
    return bookings


def select(gym_class_id, member_id):
    booking = None
    sql = "SELECT * FROM bookings WHERE gym_class_id = %s AND member_id=%s"
    values = [gym_class_id, member_id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        booking = Booking(result['member_id'],result['gym_class_id'],result['id'])
    return booking

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)