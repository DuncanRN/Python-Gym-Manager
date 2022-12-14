from flask import request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository

import repositories.member_repository as member_repository

bookings_blueprint = Blueprint("booking", __name__)

# CREATE
# POST '/classes'
@bookings_blueprint.route("/bookings", methods=['POST'])
def create_booking():
    member_id = request.form['member_id']
    gym_class_id = request.form['gym_class_id']
    redirect_to = request.form['redirect_to']

    booking = Booking(member_id, gym_class_id)
    # check how many people are in the class.
    # if that's equal to the capacity, redirect to an error page
    # else save this booking
    this_gym_class = gym_class_repository.select(gym_class_id)
    members_in_class = gym_class_repository.members(gym_class_id)
    this_member = member_repository.select(member_id)

    membership_level= member_repository.select(member_id).membership

    daytime_of_class = this_gym_class.date_start
    hour_of_class = daytime_of_class.hour

    

    if len(members_in_class) == this_gym_class.capacity:
        return redirect('classes/error_message/0') # error message 0 will be a class at capacity error
    elif membership_level=="Standard" and hour_of_class>16 and hour_of_class<20:
        return redirect('classes/error_message/1') # error message 1 will be a peak time / standard membership problem
    elif this_member.active != True:
        return redirect('classes/error_message/2') # error message 2 is "member is deactivated"
    elif this_gym_class.status=="Deactivated":
        return redirect('classes/error_message/3') # error message 3 is "class is deactivated"
    else:
        booking_repository.save(booking)
        if redirect_to=="classes":
            return redirect('/classes/'+gym_class_id)
        else:
            return redirect('/members/'+member_id)
    

# DELETE
# DELETE (acutally GET) '/bookings/13/16/delete'
@bookings_blueprint.route("/bookings/<gym_class_id>/<member_id>/delete", methods=['GET'])
def delete_booking(gym_class_id, member_id):
    booking = booking_repository.select(gym_class_id, member_id)
    booking_repository.delete(booking.id)
    
    return redirect('/classes/'+gym_class_id)