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

member_1 = Member("Peter", "La Fleur")
member_repository.save(member_1)

member_2 = Member("Patches", "OHoulihan")
member_repository.save(member_2)

member_3 = Member("White", "Goodman")
member_repository.save(member_3)

gym_class_1 = GymClass("Dodge, Duck, Dip, Dive and Dodge")
gym_class_repository.save(gym_class_1)
gym_class_2 = GymClass("Swimming for Beginners")
gym_class_repository.save(gym_class_2)
gym_class_3 = GymClass("Strength and Conditioning")
gym_class_repository.save(gym_class_3)

booking_1 = Booking(member_1.id, gym_class_1.id)
booking_repository.save(booking_1)
booking_2 = Booking(member_1.id, gym_class_2.id)
booking_repository.save(booking_2)
booking_3 = Booking(member_1.id, gym_class_3.id)
booking_repository.save(booking_3)
booking_4 = Booking(member_2.id, gym_class_1.id)
booking_repository.save(booking_4)
booking_5 = Booking(member_3.id, gym_class_1.id)
booking_repository.save(booking_5)
