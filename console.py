from models.member import Member
from models.gym_class import GymClass
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.booking_repository as booking_repository

member_repository.delete_all()
gym_class_repository.delete_all()
booking_repository.delete_all()


member_1 = Member("Mr", "Pink", "Premium", True)
member_repository.save(member_1)

member_2 = Member("Tony" , "Soprano", "Premium", True)
member_repository.save(member_2)

member_3 = Member("Michael", "Corleone", "Standard", True)
member_repository.save(member_3)

member_4 = Member("Vito", "Corleone", "Premium", True)
member_repository.save(member_4)

member_5 = Member("Jimmy", "Hoffa", "Standard", True)
member_repository.save(member_5)

member_6 = Member("Frank", "Sheeran", "Standard", False)
member_repository.save(member_6)

member_7 = Member("Karen", "Hill", "Standard", True)
member_repository.save(member_7)

member_8 = Member("Kay", "Adams-Corleone", "Standard", True)
member_repository.save(member_8)

gym_class_1 = GymClass("Swimming (with the fishes) for Beginners", "2023-01-01 14:30:00", 'Monthly', "2023-06-01 00:00:01", 5, "Active")
gym_class_repository.save(gym_class_1)
gym_class_2 = GymClass("Shakedowns and Protein Shakes", "2022-11-01 09:30:00", 'None', "1970-01-01 00:00:01", 2, "Active")
gym_class_repository.save(gym_class_2)
gym_class_3 = GymClass("Strength and Conditioning",  "2022-06-01 12:15:00", 'None', "1970-01-01 00:00:01", 3, "Deactivated")
gym_class_repository.save(gym_class_3)
gym_class_3 = GymClass("Take your shot",  "2022-06-02 14:45:00", 'None', "1970-01-01 00:00:01", 3, "Active")
gym_class_repository.save(gym_class_3)
gym_class_3 = GymClass("Pistol Whiping ",  "2022-11-21 18:30:00", 'None', "1970-01-01 00:00:01", 5, "Active")
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
 