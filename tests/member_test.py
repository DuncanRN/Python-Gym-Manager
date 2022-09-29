import unittest
from models.member import Member

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.member_1 = Member("James", "Smith", "Premium", True, 1)
        self.member_2 = Member("Jane", "Jones", "Standard", False, 2)
        

    def test_member_has_a_first_name(self):
        self.assertEqual("James", self.member_1.first_name)

    def test_member_has_a_membership_level(self):
        self.assertEqual("Standard", self.member_2.membership)
        