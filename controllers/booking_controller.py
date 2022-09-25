from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
# import repositories.gym_class_repository as gym_class_repository
# import repositories.member_repository as member_repository

bookings_blueprint = Blueprint("booking", __name__)

# CREATE
# POST '/classes'
@bookings_blueprint.route("/bookings", methods=['POST'])
def create_booking():
    member_id = request.form['member_id']
    gym_class_id = request.form['gym_class_id']
    booking = Booking(member_id, gym_class_id)
    booking_repository.save(booking)
    return redirect('/classes')

