import pdb
from models.member import Member
from models.gym_class import GymClass
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.booking_repository as booking_repository

member_repository.delete_all()
gym_class_repository.delete_all()
booking_repository.delete_all()