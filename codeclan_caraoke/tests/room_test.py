import unittest
from classes.guest import Guest
from classes.song import Song
from classes.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Room1", 3, 1.00)
        self.room2 = Room("Room2", 5, 2.00)
        self.song = Song("Big Pimpin'", "JayZ")
        self.song2 = Song("Limbo", "Royal Blood")
        self.song3 = Song("Who let the dogs out", "Baha Men")
        self.guest = Guest("Drew", 20.00, self.song)
        self.guest2 = Guest("Gemma", 10.00, self.song2)
        self.guest3 = Guest("Harley", 5.00, self.song3)

    def test_create_room(self):
        self.assertEqual("Room1", self.room.room)

    def test_check_in_guest(self):
        self.room.check_in_guest(self.guest)

        self.assertEqual(1, len(self.room.guests))

    def test_check_in_guest_need_more_money(self):
        self.guest4 = Guest("Mr. Poor", 0.00, Song("Pls give me me money", "Naecash"))

        self.assertEqual(
            "Sorry, you don't have enough money", self.room.check_in_guest(self.guest4)
        )

    def test_check_out_guest(self):
        self.room.check_in_guest(self.guest)
        self.room.check_out_guest(self.guest)

        self.assertEqual(0, len(self.room.guests))

    def test_add_song_to_room(self):
        self.room.add_song_to_room(self.song)

        self.assertEqual(1, len(self.room.songs))

    def test_remove_song_from_room(self):
        self.room.add_song_to_room(self.song)
        self.room.add_song_to_room(self.song)
        self.room.remove_song_from_room(self.song)
        self.room2.add_song_to_room(self.song2)
        self.room2.add_song_to_room(self.song)

        self.assertEqual(1, len(self.room.songs))
        self.assertEqual(2, len(self.room2.songs))

    def test_is_room1_full(self):
        self.room.check_in_guest(self.guest)
        self.room.check_in_guest(self.guest2)
        self.room.check_in_guest(self.guest3)

        self.assertEqual("Sorry this room is full", self.room.is_room_full())
        self.assertEqual(False, self.room2.is_room_full())

    def test_is_room2_full(self):
        self.room2.check_in_guest(self.guest)
        self.room2.check_in_guest(self.guest2)
        self.room2.check_in_guest(self.guest3)
        self.room2.check_in_guest(self.guest3)
        self.room2.check_in_guest(self.guest3)

        self.assertEqual("Sorry this room is full", self.room2.is_room_full())
        self.assertEqual(False, self.room.is_room_full())

    def test_guest_favourite_song(self):
        self.room.add_song_to_room(self.song)
        self.room.add_song_to_room(self.song2)
        self.room.add_song_to_room(self.song3)

        self.assertEqual("Whoo!", self.room.guest_favourite_song(self.guest))

    def test_room_total(self):
        self.room.check_in_guest(self.guest)
        self.room.check_in_guest(self.guest2)
        self.room.check_in_guest(self.guest3)
        self.guest.wallet_reduced(self.room)
        self.guest2.wallet_reduced(self.room)
        self.guest3.wallet_reduced(self.room)
        self.room.add_money_to_room()
        self.room.add_money_to_room()
        self.room.add_money_to_room()

        self.assertEqual(3, self.room.room_money)
        self.assertEqual(19, self.guest.wallet)
        self.assertEqual(9, self.guest2.wallet)
        self.assertEqual(4, self.guest3.wallet)

    def test_room2_total(self):
        self.room2.check_in_guest(self.guest)
        self.room2.check_in_guest(self.guest2)
        self.room2.check_in_guest(self.guest3)
        self.guest.wallet_reduced(self.room2)
        self.guest2.wallet_reduced(self.room2)
        self.guest3.wallet_reduced(self.room2)
        self.room2.add_money_to_room()
        self.room2.add_money_to_room()
        self.room2.add_money_to_room()

        self.assertEqual(6, self.room2.room_money)
        self.assertEqual(18, self.guest.wallet)
        self.assertEqual(8, self.guest2.wallet)
        self.assertEqual(3, self.guest3.wallet)

    def test_request_a_song(self):
        self.room.request_a_song()

        self.assertEqual(1, len(self.room.songs))
