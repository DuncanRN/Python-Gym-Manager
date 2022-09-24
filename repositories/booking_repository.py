from db.run_sql import run_sql
from models.booking import Booking

def save(booking):
    sql = "INSERT INTO bookings ( member_id, gym_class_id) VALUES ( %s, %s) RETURNING id"
    values = [booking.member_id, booking.gym_class_id]   

    results = run_sql( sql, values )
    booking.id = results[0]['id']
    return booking


def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        booking = Booking(row['member_id'], row['gym_class_id'], row['id'])
        bookings.append(booking)
    return bookings


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)
