from db.run_sql import run_sql
from models.booking import Booking
# import repositories.user_repository as user_repository
# import repositories.location_repository as location_repository

def save(booking):
    sql = "INSERT INTO bookings ( member_id, class_id) VALUES ( %s, %s) RETURNING id"
    values = [booking.member_id, booking.class_id]   
    # above here, we could do booking.member.id and booking.class.id
    # because we'd store the whole user and the whole class in the booking... But do we want to do that?
    #  negative - storing the class and the memeber name in the booking, if either changes... like the time or the 
    #  name of a class, it'd remain unchanged in the booking.....
    # 
    #  I thinkwe should stick with just the class id and member id inside booking
    # the output of bookings needs to be rethought though...

    # no actually it's ok, it can just call the member def select(id): as select(member). 
    # that's still pretty clean

    results = run_sql( sql, values )
    booking.id = results[0]['id']
    return booking


def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:

        #  HERE
        user = user_repository.select(row['user_id'])
        location = location_repository.select(row['location_id'])
        booking = Booking(user, location, row['review'], row['id'])
        bookings.append(booking)
    return bookings


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)
