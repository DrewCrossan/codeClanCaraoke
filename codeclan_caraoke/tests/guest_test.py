import unittest
from classes.guest import Guest
from classes.song import Song
from classes.room import Room


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.song = Song("Streets", "Doja Cat")
        self.guest = Guest("Gemma", 10.00, self.song)

    def test_create_guest(self):
        self.assertEqual("Gemma", self.guest.name)
        self.assertEqual(10.00, self.guest.wallet)
        self.assertEqual(self.song, self.guest.fav_song)

    def test_wallet_reduced(self):
        self.guest.wallet_reduced(Room("Room1", 3, 1))
        self.guest.wallet_reduced(Room("Room2", 5, 2))

        self.assertEqual(7.00, self.guest.wallet)
