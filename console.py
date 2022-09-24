import pdb
from models.member import Member
from models.class import Class
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.class_repository as class_repository
import repositories.booking_repository as booking_repository

member_repository.delete_all()
class_repository.delete_all()
booking_repository.delete_all()